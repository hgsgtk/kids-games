#!/usr/bin/env python3
"""
Local server for Kids Games: serves static files and records game click counts in SQLite3.
Run: python server.py
Then open http://127.0.0.1:5000/
"""
import os
import sqlite3
from pathlib import Path

from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__, static_folder=".", static_url_path="")
BASE = Path(__file__).resolve().parent
DB_PATH = BASE / "game_clicks.db"


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    with get_db() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS game_clicks (
                game_id TEXT PRIMARY KEY,
                clicks INTEGER NOT NULL DEFAULT 0
            )
            """
        )
        conn.commit()


@app.route("/api/click", methods=["POST", "GET"])
def record_click():
    """Record a click for a game. Query param: game (e.g. abc-bouncing-balls.html)."""
    game = request.args.get("game", "").strip()
    if not game or ".." in game or "/" in game:
        return jsonify({"ok": False, "error": "invalid game"}), 400
    with get_db() as conn:
        conn.execute(
            """
            INSERT INTO game_clicks (game_id, clicks) VALUES (?, 1)
            ON CONFLICT(game_id) DO UPDATE SET clicks = clicks + 1
            """,
            (game,),
        )
        conn.commit()
    return jsonify({"ok": True, "game": game})


@app.route("/api/stats")
def get_stats():
    """Return all game click counts, sorted by clicks descending."""
    with get_db() as conn:
        rows = conn.execute(
            "SELECT game_id, clicks FROM game_clicks ORDER BY clicks DESC"
        ).fetchall()
    return jsonify([{"game_id": r["game_id"], "clicks": r["clicks"]} for r in rows])


@app.route("/")
def index():
    return send_from_directory(BASE, "index.html")


@app.route("/<path:path>")
def static_file(path):
    return send_from_directory(BASE, path)


if __name__ == "__main__":
    init_db()
    app.run(host="127.0.0.1", port=5000, debug=True)
