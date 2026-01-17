# Development Tools

This directory contains development tools for the Kids Games Collection.

## Screenshot Tool

Automated screenshot tool for capturing game screenshots.

### Prerequisites

```bash
# Create virtual environment (first time only)
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate  # On macOS/Linux
# or
venv\Scripts\activate  # On Windows

# Install dependencies
pip install playwright
playwright install chromium
```

### Usage

Make sure the local server is running on port 8000:

```bash
# In a separate terminal
python3 -m http.server 8000
```

Then run the screenshot tool:

```bash
# Take screenshots of all games
python tools/take_screenshots.py --all

# Take screenshot of a specific game
python tools/take_screenshots.py --game abc-bouncing-balls.html

# Use custom port
python tools/take_screenshots.py --all --port 3000

# Use custom output directory
python tools/take_screenshots.py --all --output img/screenshots

# Custom viewport size
python tools/take_screenshots.py --all --width 1920 --height 1080
```

### Configuration

Edit `tools/screenshot_config.json` to add or modify games:

```json
{
  "games": [
    {
      "file": "my-new-game.html",
      "wait_time": 2,
      "description": "My New Game"
    }
  ]
}
```

Parameters:
- `file`: The HTML filename
- `wait_time`: Seconds to wait before taking screenshot (for animations to start)
- `description`: Human-readable description

### Adding a New Game

1. Create your new game HTML file (e.g., `my-new-game.html`)
2. Add an entry to `tools/screenshot_config.json`:
   ```json
   {
     "file": "my-new-game.html",
     "wait_time": 2,
     "description": "My New Game"
   }
   ```
3. Run the screenshot tool:
   ```bash
   python tools/take_screenshots.py --game my-new-game.html
   ```
4. Update `index.html` to include the new game with its screenshot

### Troubleshooting

**Issue**: Browser fails to connect
- Make sure the local server is running on the correct port
- Check if the port is already in use: `lsof -ti:8000`

**Issue**: Screenshots are blank
- Increase the `wait_time` in the config
- Check browser console for errors in the game

**Issue**: Module not found
- Make sure the virtual environment is activated
- Reinstall dependencies: `pip install playwright && playwright install chromium`
