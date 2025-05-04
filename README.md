# 2048 Game 🎮

**Author**: Ahmad Shaito  
**Technology**: Python + Tkinter  

## 📝 Executive Summary

This project is a Python implementation of the classic 2048 game, developed using the `Tkinter` library for GUI support. Players interact with the game through arrow keys, sliding and combining tiles on a 4x4 grid to reach the winning tile: **2048**. The implementation features full functionality including score tracking, dynamic tile generation, game over/win detection, and a user-friendly interface.

---

## 🎯 Introduction

The goal of this project was to recreate the well-known 2048 puzzle game using Python's built-in GUI library, `Tkinter`. The game challenges users to combine tiles of equal value by sliding them across the grid until the target value (2048) is reached. This project demonstrates logic design, matrix manipulation, and interface development in Python.

---

## ⚙️ Implementation Details

### a. GUI Creation

- Built using `Tkinter`
- Includes a 4x4 game board, a score display, and a **Reset** button
- Dynamic coloring and font changes based on tile values

### b. Matrix Manipulation

- The game board is implemented as a 4x4 matrix (list of lists)
- Key functions include:
  - `stack`: moves tiles to one side
  - `combine`: merges tiles with the same value
  - `reverse`: reverses the row/column
  - `transpose`: rotates the grid

### c. Tile Generation

- After each move, a random empty cell is selected
- A new tile with value **2** or **4** is generated

### d. GUI Update

- Tiles are visually updated in real-time
- Different colors and fonts are used based on the tile number
- Score is updated after each successful combination

---

## 🎮 Gameplay

- Use **arrow keys** to move tiles: Up, Down, Left, Right
- When two tiles with the same number touch, they **combine** into one
- The goal is to create a tile with the number **2048**
- The game ends if there are no more valid moves

---

## ✅ Conclusion

The project successfully replicates the core mechanics and interface of the original 2048 game. It demonstrates effective use of GUI programming, matrix operations, and user interaction in Python. Challenges faced included efficient tile merging logic and maintaining consistent GUI updates.

---

## 💡 Recommendations for Future Work

To enhance the user experience, consider implementing:

- 🏆 High score leaderboard (local or online)
- 🌈 Theme customization or improved graphics
- 🧩 Different game modes (e.g., 5x5 board, time-limited mode)
- 📱 Mobile-friendly version using `Kivy` or other cross-platform frameworks

---

## 🚀 How to Run the Project

1. Make sure you have Python installed (version 3.6+ recommended)
2. Clone or download this repository
3. Run the game with:

```bash
python 2048.py
