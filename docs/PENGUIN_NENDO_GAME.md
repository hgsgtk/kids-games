# 🐧 Penguin Nendo Game

## Overview
A creative clay-sculpting game where kids shape "nendo" (ねんど / play-doh / clay) into an adorable penguin through 8 progressive steps.

## Theme
**Penguin + Nendo (Clay)** - Combines the cuteness of penguins with the satisfying tactile experience of molding clay.

## Gameplay

### 8 Sculpting Steps
Each step requires **10 taps/clicks** to complete:

1. **Step 0**: Warm up the clay blob 🫳
2. **Step 1**: Shape the body (dark gray with white belly) 🫳
3. **Step 2**: Add the head on top 🟤
4. **Step 3**: Press in the eyes and cheeks 👀
5. **Step 4**: Pinch the orange beak 🔶
6. **Step 5**: Pull out the wings 🪽
7. **Step 6**: Add little feet 🦶
8. **Step 7**: Final touch - cute bow tie 🎀

### Progression System
- Visual step indicator with emoji icons
- Progress bar showing overall completion (0-100%)
- Tap counter for current step (X / 10)
- Penguin counter (collection of completed penguins)

## Features

### 🎨 Visual Design
- **Snowy theme**: Light blue gradient background with falling snowflakes
- **CSS-only penguin**: Entirely built with CSS (no images)
  - Radial gradients for 3D effect on body and head
  - White belly with gradient
  - Orange beak and feet with gradients
  - Cute eyes with pupils and shine
  - Pink blush cheeks
  - Red bow tie accessory
- **Clay workspace**: Gray circular crafting area with subtle texture
- **Smooth animations**: Each part fades in with elastic bezier curves
- **Squishy effects**: Parts deform/squish on tap for tactile feedback

### 🎵 Audio Feedback
- **Squishy sounds**: Web Audio API generates pitch-varying "squish" on each tap
- **Step completion chime**: 3-note ascending melody
- **Victory fanfare**: 4-note C major arpeggio (C5-E5-G5-C6)

### 🎉 Celebration
When penguin is complete:
- Penguin dances (rotation + vertical bounce animation)
- Wings flap (alternating rotation animation)
- Full-screen achievement overlay with glow effect
- Confetti explosion (80 pieces, various colors)
- Star burst (16 stars/emojis radiating outward)
- Multiple sound effects

### 🎮 Interaction
- **Click/Tap**: Main interaction on workspace
- **Space key**: Alternative input for taps
- **Responsive**: Scales for mobile and desktop
- **Visual feedback**:
  - Clay particles scatter on each tap
  - Floating encouragement text ("Nice!", "Great!", etc.)
  - Parts squish/bounce with animations

### 🌐 Internationalization (i18n)
Built-in language switcher with full translations:

#### English
- "Shape clay into a cute penguin!"
- Step instructions: "Tap the clay to warm it up!", "Shape the body!", etc.
- Encouragement: "Nice!", "Great!", "Keep going!", "Almost there!", "Perfect!"
- Completion: "🎉 Your penguin is complete! 🐧"

#### Japanese (日本語)
- "ねんどでかわいいペンギンをつくろう！"
- Step instructions: "ねんどをタップしてやわらかくしよう！", "からだをつくろう！", etc.
- Encouragement: "いいね！", "すごい！", "がんばれ！", "あとすこし！", "かんぺき！"
- Completion: "🎉 ペンギンのかんせい！ 🐧"

### 📊 Progress Tracking
- **Step indicator**: 8 circular dots with emoji icons
  - Gray (not started)
  - Blue with glow (current step)
  - Green (completed)
- **Progress bar**: 0-100% with color transitions
  - Blue (0-59%)
  - Blue-cyan (60-99%)
  - Green (100%)
- **Penguin gallery**: Collect up to 5 penguins

### 🎨 Decorative Elements
- **Animated decorations**: Floating penguins, snowflakes, snowman, ice, mountain, fish
- **Continuous snowfall**: Random snowflakes falling throughout game
- **Clay particles**: Scatter on each tap with physics

## Technical Details

### Technologies
- **Pure HTML/CSS/JavaScript** (no frameworks)
- **Web Audio API** for sound generation
- **CSS animations** for all visual effects
- **i18n.js** for localization
- **Responsive design** with media queries

### File Structure
```
penguin-nendo-game.html    48.4 KB (self-contained game)
screenshots/
  penguin-nendo-game.png   65.9 KB (SVG-generated screenshot)
```

### Performance
- Lightweight (< 50KB)
- No external dependencies (except shared i18n.js)
- CSS-only graphics (no image loading)
- Efficient audio synthesis

## Game Stats (in index.html)
- **Category**: 🎨 Creative
- **Total Games**: Now 12 games in collection
- **Target Audience**: Kids (3-8 years old)
- **Skills**: Fine motor control, following instructions, creativity

## User Experience

### For Young Kids (3-5 years)
- Simple tap-to-progress mechanic
- Clear visual feedback on every tap
- No time pressure or failure states
- Colorful, friendly penguin character
- Celebration and positive reinforcement

### For Older Kids (6-8 years)
- Challenge to complete penguin quickly
- Collect multiple penguins (up to 5 in gallery)
- Learn step-by-step construction process
- Satisfying squish sounds and effects

## Educational Value
- **Sequencing**: Following 8 steps in order
- **Counting**: 10 taps per step
- **Fine motor skills**: Tapping/clicking precision
- **Patience**: Completing multi-step process
- **Cause and effect**: See immediate visual feedback
- **Creativity**: Making multiple unique penguins
- **Language**: Bilingual vocabulary (body parts, actions)

## Design Philosophy
Inspired by:
- **Mochitsuki Game**: Progressive tapping mechanic with visual transformation
- **Real clay sculpting**: Step-by-step construction mimics actual clay work
- **Kawaii aesthetic**: Cute, friendly, non-threatening visuals
- **Tactile feedback**: Squishy sounds and squash animations feel satisfying

## Future Enhancement Ideas
- More animals to sculpt (bear, cat, rabbit, etc.)
- Color picker for custom penguin colors
- Save/share completed penguins
- Photo mode to take pictures with penguins
- Background/scene customization
- Different bow tie/accessory options
- Multi-touch for faster tapping
- Achievement badges for milestones

---

**Created**: 2026-06-15  
**Status**: ✅ Complete and deployed to `dist/`  
**Play**: Open `dist/penguin-nendo-game.html` in browser
