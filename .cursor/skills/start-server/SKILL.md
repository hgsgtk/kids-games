---
name: start-server
description: Start the local development server for the Kids Games project. Use when the user asks to start, run, or launch the server, or wants to preview/test the games locally.
---

# Start Server

## Steps

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Start the Flask server in the background:

```bash
python server.py
```

3. The server runs at **http://127.0.0.1:5000/**. Let the user know it is ready.

## Notes

- The server serves static HTML game files and provides click-tracking APIs (`/api/click`, `/api/stats`).
- Game click counts are stored in `game_clicks.db` (SQLite); the file is created automatically on first run.
- If port 5000 is already in use, check for an existing process and let the user know.
