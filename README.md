# 🎮 Kids Learning Games Collection

A collection of fun, educational browser-based games for young learners. Features alphabet typing, number counting, 3D/4D adventures, interactive experiences, and special seasonal games (like the Japanese New Year mochi pounding and kite flying games) designed for children ages 2-8. No installation required!

## 🎯 Games

- **ABC Song with Bouncing Balls** - Learn the alphabet with music and interactive balls
- **Baby's 4D Wonder World** - Tap to create cute animations with sounds
- **Alphabet Typing A→Z** - Practice typing all 26 letters
- **Number Typing Game** - Count and type numbers from 0-200
- **3D Number Typing Adventure** - Immersive 3D number learning in space
- **4D Number Journey** - Numbers fly towards you in stunning 4D effects
- **Elevator Game - Kids Tower 100** - Explore 100 themed floors with real photos
- **Mochitsuki Game** - Japanese New Year mochi pounding game
- **Kite Flying Number Game** - Traditional kite flying with number learning
- **Animal Catch Game** - Catch cute animals game
- **Moomin Valley Adventure** - Help Moomin collect treasures in the magical valley

## 🚀 Getting Started

1. Clone or download this repository
2. Open `index.html` in a web browser (or use the optional server below)
3. Click on any game to start playing!

### Optional: Local server (click tracking & popularity order)

To save game click counts in SQLite and show games in **popularity order** on the top page:

```bash
npm install
npm start
# Open http://127.0.0.1:5000/
```

Or with auto-reload during development:

```bash
npm run dev
```

The server (Hono + better-sqlite3) creates `kids_games.db` (SQLite3) in the project root and updates it when you click a game. The top page loads `/api/stats` and sorts the game cards by click count (most popular first).

For development without click tracking:

```bash
# Start a simple HTTP server
npx serve .
```

## 📁 Project Structure

```
kids-games/
├── index.html              # Main menu page
├── server.js               # Optional: Hono server for click tracking (SQLite3)
├── package.json            # Node.js deps (Hono, better-sqlite3)
├── *.html                   # Individual game files
├── screenshots/             # Game screenshots for the menu
├── assets/
│   └── sounds/              # Audio files (door sounds, etc.)
└── tools/                   # Development tools
    ├── take_screenshots.py  # Screenshot automation tool
    ├── screenshot_config.json
    └── README.md
```

## 🛠️ Development Tools

### Screenshot Tool

Automated tool for capturing game screenshots:

```bashc
# Activate virtual environment
source venv/bin/activate

# Take screenshots of all games
python tools/take_screenshots.py --all

# Take screenshot of a specific game
python tools/take_screenshots.py --game abc-bouncing-balls.html
```

See [tools/README.md](tools/README.md) for detailed documentation.

### Adding a New Game

1. Create your new game HTML file (e.g., `my-new-game.html`)
2. Add an entry to `tools/screenshot_config.json`
3. Take a screenshot: `python tools/take_screenshots.py --game my-new-game.html`
4. Update `index.html` to include the new game card
5. Test in the browser!

## 🎨 Features

- ✨ No installation required - runs in any modern browser
- 🎵 Interactive sound effects and music
- 🎨 Colorful, kid-friendly designs
- 📱 Responsive layouts for mobile and desktop
- 🌏 **Multilingual support** (English and Japanese) - Select games support language switching
- 🎮 3D graphics with Three.js
- 🏆 Progress tracking and achievements

### 🌐 Multi-language Support

All Japanese-themed games now support both English and Japanese with a convenient language switcher button in the top-right corner:

- ✅ **Elevator Game (Kids Tower 100)** - Full bilingual support with comprehensive UI translation
- ✅ **Mochitsuki Game** - Mochi pounding game with bilingual interface
- ✅ **Kite Flying Number Game (Tako-age)** - Traditional New Year's game in both languages
- ✅ **Animal Catch Game** - Number learning game with language options

**Features:**
- 🔄 Easy language switching with a single click
- 💾 Language preference is automatically saved
- 🎯 All UI elements, buttons, and messages are translated
- 🌍 Seamless experience in both languages

The language preference is saved locally and will be remembered for your next visit!

## 🧪 Browser Compatibility

- Chrome/Edge (recommended)
- Firefox
- Safari
- Mobile browsers (iOS Safari, Chrome Mobile)

## 📝 License

See [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Add new games
- Improve existing games
- Fix bugs
- Enhance documentation

---

✨ Made with love for young learners! ✨
