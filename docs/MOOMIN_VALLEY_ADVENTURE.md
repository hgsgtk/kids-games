# 🌸 Moomin Valley Adventure 🌸

An interactive adventure game where players help Moomin explore the beautiful Moominvalley and collect magical treasures!

## 🎮 Game Features

### Core Gameplay
- **Click-to-Move**: Click anywhere in the valley to move Moomin to that location
- **Treasure Collection**: Collect 15 different types of treasures scattered around the valley
- **Time Challenge**: Complete the collection within 60 seconds
- **Auto-Collection**: Treasures are automatically collected when Moomin gets close enough

### Visual Features
- ✨ **Beautiful Scenery**: Animated clouds floating across a gradient sky
- ☀️ **Pulsing Sun**: Dynamic sun animation
- 🌳 **Decorated Valley**: Trees and colorful flowers throughout the scene
- 🎨 **Particle Effects**: Sparkling particle animations when collecting treasures
- 🦡 **Cute Moomin Character**: Fully animated Moomin character with hover effects

### Audio Features
- 🔊 **Sound Effects**: 
  - Movement sounds when clicking
  - Collection sounds with melodic notes (C5 → E5)
  - Victory fanfare (C-D-E-G progression)
- 🔇 **Sound Toggle**: Easy on/off button for audio

### Treasure Types
The game features 13 different treasure emojis:
- 🌟 Stars
- 💎 Gems
- 🎁 Gifts
- 🌺 Flowers
- 🍄 Mushrooms
- 🦋 Butterflies
- 🐚 Seashells
- 🎨 Art palettes
- 🎭 Masks
- 🎪 Circus tents
- 🎡 Ferris wheels
- 🎠 Carousels
- 🎢 Roller coasters

## 🎯 Game Objectives

1. **Move Moomin**: Click on the screen to guide Moomin around the valley
2. **Collect Treasures**: Click on treasures or move near them to collect
3. **Beat the Clock**: Collect 15 treasures before time runs out
4. **Celebrate Victory**: Enjoy the victory animation and play again!

## 🎨 Design Highlights

### Color Scheme
- Sky: Gradient from sky blue (#87CEEB) through mint (#98D8C8) to light green (#90EE90)
- Moomin: Classic white with black outlines
- UI Elements: Soft pinks (#FF6B9D) and blues (#2E5266)

### Animation Effects
1. **Floating Clouds**: Three clouds drift across the screen at different speeds
2. **Bouncing Treasures**: Treasures gently bounce up and down
3. **Swaying Flowers**: Ground flowers sway in the breeze
4. **Pulsing Sun**: The sun gently pulses in size
5. **Particle Burst**: 10 sparkles burst out when collecting treasures

### Responsive Design
- Adapts to different screen sizes
- Maintains aspect ratio and gameplay area
- Touch-friendly for mobile devices

## 👥 Target Audience

- **Age Range**: 4-8 years old
- **Skills Developed**:
  - Hand-eye coordination
  - Mouse/touch control
  - Time management
  - Goal-oriented gameplay
  - Pattern recognition

## 🎵 Technical Details

### Sound Implementation
Uses Web Audio API for:
- Dynamic sound generation
- No external audio files needed
- Adjustable frequencies and durations
- Exponential gain ramping for smooth fade-outs

### Performance
- Efficient DOM manipulation
- CSS-based animations for smooth 60fps
- Minimal JavaScript for game logic
- No external dependencies

## 🎪 Game States

1. **Initialize**: Game loads, Moomin positioned, initial treasures spawn
2. **Playing**: Player moves Moomin, collects treasures, timer counts down
3. **Victory**: 15 treasures collected before time runs out
4. **Game Over**: Time expires before reaching goal
5. **Restart**: Reset all states and start fresh

## 🔧 Customization Options

Easy to modify:
- `timeLeft`: Adjust time limit (default: 60 seconds)
- `targetScore`: Change number of treasures to collect (default: 15)
- `treasures` array: Add or remove treasure types
- Speed and difficulty can be adjusted in the code

## 📱 Browser Compatibility

- ✅ Chrome/Edge (recommended)
- ✅ Firefox
- ✅ Safari
- ✅ Mobile browsers (iOS Safari, Chrome Mobile)

## 🎁 Special Features

- **Instructions**: Auto-fading instructions appear on first load
- **Home Button**: Easy navigation back to game collection
- **Sound Toggle**: Persistent sound preference
- **Victory Screen**: Celebratory message with replay option
- **Collection Display**: Visual tracker of collected treasures

## 🌟 Future Enhancement Ideas

- Multiple difficulty levels
- Different valley themes (winter, autumn, night)
- More Moomin characters to play as
- Achievement system
- High score leaderboard
- Power-ups and special abilities
- Story mode with multiple levels

---

**Made with ❤️ for Moomin fans and young adventurers!**
