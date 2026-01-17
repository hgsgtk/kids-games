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

## 🚀 Getting Started

1. Clone or download this repository
2. Open `index.html` in a web browser
3. Click on any game to start playing!

For development:

```bash
# Start a local server
python3 -m http.server 8000

# Open in browser
open http://localhost:8000/
```

## 📁 Project Structure

```
kids-games/
├── index.html              # Main menu page
├── *.html                  # Individual game files
├── screenshots/            # Game screenshots for the menu
├── assets/
│   └── sounds/            # Audio files (door sounds, etc.)
├── tools/                  # Development tools
│   ├── take_screenshots.py       # Screenshot automation tool
│   ├── screenshot_config.json    # Screenshot configuration
│   └── README.md                 # Tools documentation
└── venv/                   # Python virtual environment (local only)
```

## 🛠️ Development Tools

### Screenshot Tool

Automated tool for capturing game screenshots:

```bash
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
