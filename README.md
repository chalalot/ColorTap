# Jungle Safari: Animal Escape - Playable Ad

A web-based playable advertisement for the mobile puzzle game "Color Tap: Unblock Puzzle". This interactive HTML5 game showcases chain reaction mechanics where players click blocks to trigger sequential movements in arrow directions.

## Features

- **Chain Reaction Mechanics**: Click aligned arrow blocks to trigger sequential removal from outermost to innermost
- **Shape Selection Menu**: Choose between Round Safari (circle), Classic Safari (rectangle), and Peak Safari (triangle)
- **Responsive Design**: Optimized for both mobile and desktop devices
- **Jungle Theme**: Immersive rainforest atmosphere with animal backgrounds
- **Connected Puzzle Generation**: Algorithm ensures all blocks are adjacent and solvable
- **Cycle Detection**: Advanced DFS algorithm prevents impossible puzzle loops

## How to Play

1. **Start**: Select a shape from the menu (currently only rectangle is implemented)
2. **Objective**: Clear all animal blocks from the 9x9 grid
3. **Mechanics**: Click blocks to move them in their arrow direction
4. **Chain Reactions**: When blocks are aligned in arrow direction (→ (1) → (2) → (3)), clicking the first block triggers a chain that activates from outermost to innermost
5. **Win Condition**: Successfully clear all blocks from the board

## Technical Stack

- **Pure HTML5/CSS/JavaScript**: No external dependencies
- **Canvas Rendering**: HTML5 Canvas for smooth game graphics
- **Responsive Layout**: CSS Flexbox with mobile-first design
- **Algorithm Features**:
  - Connected block generation
  - DFS cycle detection
  - Chain reaction pathfinding
  - Solvability validation

## File Structure

```
├── index.html          # Complete game implementation
├── replit.md          # Technical documentation and changelog
└── README.md          # This file
```

## Development

The game is designed as a single HTML file for easy embedding in advertising platforms. To run locally:

1. Download the `index.html` file
2. Open in any modern web browser
3. No server required for basic functionality

## Browser Support

- Chrome/Edge 80+
- Firefox 75+
- Safari 13+
- Mobile browsers with touch support

## Architecture

- **Single-page application** built with vanilla web technologies
- **Canvas-based rendering** for game graphics and animations
- **Touch-optimized** interface for mobile devices
- **Modular JavaScript** architecture with clear separation of concerns

## Recent Updates

- Implemented chain reaction mechanics for sequential block triggering
- Added comprehensive cycle detection to prevent impossible puzzles
- Enhanced jungle theme with static animal backgrounds
- Refined 9x9 grid layout with connected block generation
- Added shape selection menu system with mysterious silhouettes

---

*Built for Replit deployment with mobile-first responsive design*