# Project: Terminal Dino Runner

## Overview
A terminal-based clone of the Chrome Dino Runner game, focusing on core mechanics (jumping, obstacle avoidance, scoring) using simple text-based rendering. Built for Linux with `curses` for terminal control.

## Core Concepts
1. **Terminal Rendering**
   - Use `curses` for real-time screen updates, input handling, and positioning
   - Basic symbols (`@` for dino, `|` for cacti) for initial implementation
2. **Game Loop**
   - Fixed timestep updates (e.g., 10 updates/second) for predictable physics
   - Input handling (spacebar for jump) and frame rendering in a single loop
3. **Physics Simulation**
   - Discrete velocity system with gravity and jump impulse
   - Collision detection via axis-aligned bounding boxes (AABB)
4. **Obstacle System**
   - Randomly spawning cacti with varying widths
   - Horizontal movement toward the player
5. **Scoring System**
   - Score increases with time survived
   - Displayed at top of terminal

## Architecture
```
terminal_dino/
│
├── game.py          # Main game loop and state management
├── entities.py      # Dino and Obstacle classes with physics/logic
├── renderer.py      # Terminal rendering via curses
├── config.py        # Game constants (screen size, speeds, etc.)
└── main.py          # Entry point
```

## Key Decisions
- **Symbol Representation**: Chose `@` for dino and `|` for cacti for minimal implementation complexity
- **Physics**: Discrete velocity system rather than continuous physics for simplicity
- **Rendering**: `curses` over `rich` for precise control over terminal positioning and input
- **Obstacle Spawning**: Random timer-based system (1.5-3 second intervals) for basic variety

## Known Trade-offs / Deferred Items
- **Visual Fidelity**: Basic symbols limit visual complexity but keep implementation simple
- **Cross-Platform**: Focused on Linux; Windows support would require `windows-curses` compatibility work
- **Input Latency**: Terminal input handling has inherent latency compared to GUI applications