# Color Tap: Unblock Puzzle - Playable Ad

## Overview

This project is a web-based playable advertisement for a mobile puzzle game called "Color Tap: Unblock Puzzle". It's designed as a standalone HTML5 game that can be embedded in various advertising platforms to showcase the gameplay mechanics and entice users to download the full mobile app.

## System Architecture

### Frontend Architecture
- **Pure HTML5/CSS/JavaScript**: Single-page application built with vanilla web technologies
- **Canvas-based rendering**: Uses HTML5 Canvas for game graphics and animations
- **Responsive design**: Adapts to various screen sizes and orientations for mobile and desktop
- **Touch-optimized**: Designed primarily for touch interactions on mobile devices

### Technology Stack
- HTML5 for structure
- CSS3 for styling with gradient backgrounds and modern UI elements
- JavaScript (likely) for game logic and interactivity
- HTML5 Canvas for game rendering

## Key Components

### Game Canvas
- Central game rendering area with rounded corners and shadow effects
- Responsive sizing that adapts to viewport dimensions
- Background styling with gradient effects

### UI System
- Overlay-based UI architecture using absolute positioning
- Pointer events management for selective interaction areas
- Z-index layering for proper UI element stacking

### Styling Architecture
- CSS reset for consistent cross-browser behavior
- Modern CSS features including flexbox for layout
- CSS custom properties likely used for theming
- Mobile-first responsive design approach

## Data Flow

### User Interaction Flow
1. User interacts with touch/click events on game canvas
2. Game logic processes input and updates game state
3. Canvas redraws updated game elements
4. UI overlay updates to reflect game status

### Rendering Pipeline
- Game state → Canvas rendering → Visual output
- UI state → Overlay updates → Interface feedback

## External Dependencies

### Minimal Dependencies
- No external JavaScript frameworks or libraries detected
- Self-contained codebase for fast loading
- Likely uses browser APIs for:
  - Canvas 2D rendering context
  - Touch/mouse event handling
  - Device orientation detection

## Deployment Strategy

### Playable Ad Optimization
- Single HTML file architecture for easy embedding
- Minimal asset loading for fast initialization
- Optimized for various ad network requirements
- Mobile-first design for primary target platform

### Distribution Channels
- Can be embedded in mobile ad networks
- Suitable for social media advertising
- Compatible with web-based promotional campaigns

## User Preferences

Preferred communication style: Simple, everyday language.

## Recent Changes

- July 08, 2025: Implemented chain reaction mechanics
  - Added multi-block removal system for arrow-aligned blocks
  - When clicking a free block, checks for consecutive blocks in the arrow direction (→ (1) → (2) → (3))
  - All consecutive moveable blocks pointing in same direction are triggered in sequence
  - Chain activates from outermost to innermost: 3, then 2, then 1 with staggered timing
  - Works for chains of 2, 3, 4, or more blocks in sequence
  - Enhanced visual feedback with sequential scaling and fading animations
  - Single blocks still move normally when no chain is possible

- July 08, 2025: Refined board size and added connectivity constraints
  - Adjusted grid size to 9x9 to prevent UI text overlap
  - Implemented connected block generation ensuring all blocks are adjacent to at least one other
  - Starts with seed block in center and grows outward through adjacent positions only
  - Creates more organic, connected puzzle shapes instead of scattered isolated blocks
  - Reduced block count to 15-25 blocks with connected patterns for strategic gameplay
  - Updated fallback puzzle with connected layout centered in the 9x9 grid

- July 08, 2025: Added shape selection menu system
  - Created preloader → shape menu → game flow instead of direct game start
  - Added three mysterious shape options: Round Safari (circle), Classic Safari (rectangle), Peak Safari (triangle)
  - Shapes are displayed as black silhouettes with question marks to create intrigue
  - Rectangle option leads to the current puzzle game (only one implemented)
  - Added menu navigation buttons throughout the game interface
  - Enhanced UI flow with proper state management between menu and game modes

- July 08, 2025: Complete game mechanics redesign
  - Changed from drag-and-drop unblock puzzle to click-to-move block clearing game
  - All blocks are now square (1x1) with predefined movement directions
  - Clicking a block moves it in its direction until it hits another block or flies off screen
  - Blocks that reach the edge disappear from the game
  - Win condition: clear all blocks from the board
  - Added direction arrows (↑↓←→) on each block to show movement direction
  - Updated game instructions and UI to reflect new mechanics

- July 08, 2025: Fixed movement logic and added puzzle generation
  - Fixed blocks to only move if entire path to edge is clear (no partial movements)
  - Added randomized puzzle generation that ensures solvability
  - Restart button now generates new random layouts instead of fixed puzzle
  - Added solvability checking to prevent impossible puzzle configurations
  - Generate 6-9 blocks per puzzle with varied colors and directions

- July 08, 2025: Transformed to jungle/rainforest animal theme
  - Changed game title to "Jungle Safari: Animal Escape"
  - Updated color scheme to jungle greens and earth tones
  - Replaced geometric blocks with animal emojis (tiger, lion, monkey, gorilla, elephant, parrot, etc.)
  - Added jungle gradient background with atmospheric leaf patterns
  - Increased block density to 12-16 animals per puzzle for more challenging gameplay
  - Updated UI text to reflect animal escape theme instead of block clearing
  - Direction arrows now appear as small corner indicators while animals are the main focus

- July 08, 2025: Refined jungle theme and added directional constraints
  - Moved animals to static background positions (trees, flowers, butterflies)
  - Removed noisy moving patterns for cleaner visuals
  - Made direction arrows thick, bold, and prominently displayed in block centers
  - Added two critical puzzle generation constraints:
    1. Blocks on same row/column never point toward each other (prevents mutual blocking across entire lines)
    2. Comprehensive loop detection using DFS cycle detection algorithm
  - Enhanced puzzle generation algorithm to validate constraints before placement
  - Implemented directed graph-based cycle detection that catches all loop types:
    - Small 2×2 arrow loops (→ ↓ ← ↑)
    - L-shaped loops spanning different distances
    - Long path loops across any grid size
    - Treats arrow directions as edges in a directed graph and uses DFS to detect back edges

## Changelog

- July 08, 2025: Initial setup with drag-and-drop unblock puzzle
- July 08, 2025: Redesigned to click-based block clearing game per user requirements