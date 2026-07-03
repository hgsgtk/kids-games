# ⛰️ Mountain Climb Number Game (山登りナンバーゲーム)

## Overview
A fun educational game where kids climb a mountain by typing numbers in sequential order (1-20). As they type the correct numbers, their character climbs higher up the mountain!

## Features

### 🎮 Gameplay
- **Sequential Number Learning**: Type numbers from 1 to 20 in order using keyboard
- **Visual Progress**: Watch your climber ascend the mountain with each correct answer
- **No Time Limit**: Learn at your own pace - no pressure!
- **Altitude Tracking**: Real-time altitude display (starting at 50m)
- **Dynamic Scoring**: Earn 10 points per correct number + 100 bonus for summit
- **Smart Input**: Automatically handles 1-digit and 2-digit numbers (e.g., type "1" for 1, "20" for 20)

### 🎨 Visual Elements (Full Canvas Rendering)

The entire game scene is rendered on an HTML5 Canvas with a 60fps animation loop.

- **Realistic Mountain Landscape**:
  - **Multi-layer mountain ranges** (far, mid, main) drawn with bezier curves
  - **Main mountain** with gradient from snow cap → rock → forest → grass
  - **Deterministic rocky ridge textures** for realistic surface detail
  - **Glowing snow cap** with jagged snowline and ambient glow
  - **Mode-specific color palettes**:
    - **Mode 20 (1-20)**: Bright daylight – green mountains, blue sky, sunlit
    - **Mode 30 (1-30)**: Sunset – orange/amber sky, warm brown mountains
    - **Mode 50 (1-50)**: Night – deep blue sky, dark rocky mountains, moonlit
    - **Mode 100 (1-100)**: Deep night – starfield, dark purple mountains

- **Sky & Atmosphere**:
  - **Sun**: Radial gradient glow + 12 animated rotating rays (modes 20, 30)
  - **Moon**: Craters, warm glow (modes 50, 100)
  - **120 twinkling stars**: Individual phase/speed, sine-wave opacity (night modes)
  - **Shooting stars**: Randomly spawned with fading trails
  - **6 fluffy clouds**: Multi-ellipse shapes, mode-specific colors, drifting
  - **Animated birds**: 4 birds with quadratic-curve wings, realistic flapping
  - **Fog overlay**: Subtle mode-colored atmospheric haze

- **Detailed Climber Character (Canvas-drawn)**:
  - **Bucket hat** with colored band
  - **Realistic face**: Skin tone, eyes, smile, rosy cheeks
  - **Red hiking jacket** with zipper detail
  - **Orange backpack** with straps and pocket
  - **Brown pants and hiking boots**
  - **Two hiking poles** held in hands
  - **Walking animation**: Arms and legs swing in alternating cycle
  - **Ground shadow** ellipse beneath
  - Climber follows the **zigzag trail** up the mountain

- **Zigzag Hiking Trail**:
  - 30-segment path with sine-wave switchbacks
  - Dashed line with shadow for depth
  - Numbers positioned along the trail
  - Climber smoothly interpolates position on trail

- **28 Animated Trees**:
  - Placed along both sides of the trail
  - 3-layer triangular foliage with trunk
  - Gentle wind-sway animation
  - Fade out near the peak (treeline)

- **Summit Flag**:
  - Pole with waving flag drawn via sine-wave vertices
  - Gold star on flag
  - Appears when climber reaches the top

- **Interactive Numbers**:
  - Auto-scaled based on mode (60px down to 36px)
  - Positioned along the trail path with random offset
  - Current target highlighted with pulse + golden glow
  - Collection animation with spin, scale, and fade
  - Mode-specific particle burst colors on correct answer

### 🏆 Game Mechanics
- **Correct Answer**:
  - Proportional altitude gain based on progress
  - **Enhanced particle explosion** with mode-specific colors
  - Pleasant ascending sound effect (C5 → E5 → G5)
  - Number disappears with **enhanced spin, scale, and float animation**
  - Climber smoothly moves up the mountain
  - Next number pulses with glow effect

- **Wrong Answer**:
  - Shake animation
  - Error sound effect
  - No progress or penalties - try again!

- **Summit Victory**:
  - Victory flag appears at mountain peak with wave animation
  - **Massive celebration particle burst** (30 waves of colorful confetti)
  - Special completion message
  - Game completion modal with replay options

### 🎵 Audio
- **Web Audio API** powered sound effects
  - Correct: Pleasant ascending chime (C5 → E5 → G5)
  - Wrong: Descending tone to indicate mistake
  - No external audio files needed

### 📊 Game Stats Display
- Current target number (what to type next)
- Total score
- Current altitude in meters

### 🎯 Educational Value
- **Number Recognition**: Visual identification of numbers 1-20
- **Sequential Thinking**: Understanding numerical order
- **Keyboard Skills**: Typing practice with number keys
- **Goal Achievement**: Motivation through progress visualization
- **Self-Paced Learning**: No time pressure, perfect for building confidence

### 📱 Responsive Design
- Mobile-friendly layout
- Scaled elements for smaller screens
- Touch-optimized click targets

## Technical Details

### Animation Features (60fps Canvas)
- **Full 60fps render loop** – every frame drawn on Canvas
- **Walking cycle**: Arms and legs swing with `sin(time)` for natural motion
- **Twinkling stars**: 120 stars each with unique phase and speed
- **Shooting stars**: Spawned every ~3s with fading trails
- **Sun rays**: 12 rotating rays with pulsing length
- **Cloud drift**: Smooth left-to-right with wrap-around
- **Bird flapping**: Quadratic-curve wings with sine-wave cycle
- **Tree wind sway**: Gentle oscillation based on position
- **Snow cap glow**: Ambient shadow with mode-specific color
- **Flag wave**: Sine-wave vertices for realistic cloth motion
- **Climber trail following**: Smooth interpolation along 30-segment path
- **Mode-specific particle colors**: Gold/sunset/night blue/moonlight
- **Summit celebration**: 40 waves × 6 particles with spin and gravity
- **Rocky ridge textures**: Deterministic procedural detail lines

### Game Flow
1. **Start**: Game begins when you start typing
2. **Play**: Type numbers 1-20 in sequence
3. **Climb**: Character moves up with each correct answer
4. **Summit**: Reach 20 and see the victory flag
5. **End**: Victory modal with final stats
6. **Restart**: Press Enter or click Play again button

### Browser Compatibility
- Modern browsers with CSS3 and ES6 support
- Web Audio API for sound (fallback gracefully)
- No external dependencies

## Theme & Aesthetics
- **Nature-inspired color palette**: Sky blue, forest green, mountain brown, snow white
- **Japanese mountain climbing (登山) theme**
- **Warm, encouraging atmosphere** for young learners
- **Clean, uncluttered design** focusing on the mountain and numbers

## How to Play
1. Look at the number displayed at the top ("数字 1 を入力!")
2. Type that number on your keyboard
3. Watch your climber go higher!
4. Continue typing numbers in order (1, 2, 3... 20)
5. Take your time - there's no rush!
6. Reach the summit (山頂) to win!
7. Press Enter to restart after reaching the summit
8. Get bonus points for reaching the top! 🏔️

### Keyboard Controls
- **0-9 keys**: Type numbers
- **Enter**: Restart game (when game is over)
- The game intelligently waits 0.5s for 2-digit numbers (e.g., when typing "20")

## Perfect For
- Kids ages 4-8 learning number sequences
- Practicing number recognition and typing (1-20, 1-30, 1-50, or 1-100)
- Self-paced learning without time pressure
- Building confidence with numbers and keyboard skills
- Progressive difficulty - start easy (20) and work up to (100)
- Fun indoor activity on a rainy day
- Kids who need extra time to find keys on the keyboard
- Enjoying a visually rich, relaxing mountain adventure from home!
- Experiencing different times of day through gameplay

---
**Created**: June 2026
**Theme**: 山登り (Mountain Climbing)
**Category**: Educational / Number Learning Game
