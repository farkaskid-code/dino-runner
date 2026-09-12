# Task 1: Initialize Terminal Rendering

## Concept Recap
This task establishes the foundational terminal rendering system using `curses`, creating a basic window and input handling framework that will support all subsequent game mechanics.

## Goal
Create a working terminal window with basic input handling capabilities for the game

## Inputs / Outputs
- Inputs: Keyboard events (specifically spacebar for jumping)
- Outputs: A curses-based window with proper game area dimensions

## Constraints
- Must use `curses` library for terminal control
- Window should leave room for score display at top
- Must handle keyboard input asynchronously

## Acceptance Criteria
1. [TESTABLE] The terminal window is successfully initialized with proper dimensions (e.g., 24 rows high, 80 columns wide) [TESTABLE]
2. [TESTABLE] The window properly handles keyboard input (specifically spacebar) [TESTABLE]
3. [QUALITATIVE] The window has appropriate padding for game elements and score display [QUALITATIVE]
4. [TESTABLE] The curses window is properly cleaned up on exit [TESTABLE]

## Explicitly Out of Scope
- Game logic or physics simulation
- Actual game entities (dino, obstacles)
- Scoring system implementation