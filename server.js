import { serve } from "@hono/node-server";
import { serveStatic } from "@hono/node-server/serve-static";
import { Hono } from "hono";
import Database from "better-sqlite3";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

const DB_PATH = join(__dirname, "kids_games.db");

const db = new Database(DB_PATH);
db.pragma("journal_mode = WAL");

db.exec(`
  CREATE TABLE IF NOT EXISTS game_clicks (
    game_id TEXT PRIMARY KEY,
    clicks INTEGER NOT NULL DEFAULT 0
  )
`);

const upsertClick = db.prepare(`
  INSERT INTO game_clicks (game_id, clicks) VALUES (?, 1)
  ON CONFLICT(game_id) DO UPDATE SET clicks = clicks + 1
`);

const allStats = db.prepare(
  "SELECT game_id, clicks FROM game_clicks ORDER BY clicks DESC"
);

const app = new Hono();

app.post("/api/click", (c) => {
  const game = c.req.query("game")?.trim();
  if (!game || game.includes("..") || game.includes("/")) {
    return c.json({ ok: false, error: "invalid game" }, 400);
  }
  upsertClick.run(game);
  return c.json({ ok: true, game });
});

app.get("/api/click", (c) => {
  const game = c.req.query("game")?.trim();
  if (!game || game.includes("..") || game.includes("/")) {
    return c.json({ ok: false, error: "invalid game" }, 400);
  }
  upsertClick.run(game);
  return c.json({ ok: true, game });
});

app.get("/api/stats", (c) => {
  const rows = allStats.all();
  return c.json(rows);
});

app.get("/*", serveStatic({ root: "./" }));

const port = parseInt(process.env.PORT || "5000", 10);

serve({ fetch: app.fetch, port }, (info) => {
  console.log(`Kids Games server running at http://127.0.0.1:${info.port}/`);
});
