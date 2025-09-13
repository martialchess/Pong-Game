# Pong Game (Python Turtle)

A classic **Pong game** recreation built with Python’s `turtle` module.  
Two players control paddles on the left and right sides of the screen, bouncing the ball back and forth.  
First player to reach the winning score (default = 10) wins the game.

---

## 🎮 Game Logic
- **Ball Movement:**  
  The ball moves continuously across the screen, bouncing off the top and bottom walls.
  
- **Paddle Collision:**  
  If the ball hits a paddle, it bounces back and slightly increases in speed to make rallies more challenging.
  
- **Scoring:**  
  - If the ball passes the **right wall**, the **left player** scores.  
  - If the ball passes the **left wall**, the **right player** scores.  
  - The game resets the ball to the center after each point.

- **Winning Condition:**  
  The game ends when a player reaches **10 points**, displaying the winner in the center of the screen.

---

## 🧩 Concepts & Functionalities Covered
- Object-Oriented Programming (OOP) in Python
  - `Paddle` class (controls movement & position)
  - `Ball` class (handles velocity, bouncing, and reset)
  - `Scoreboard` class (tracks and displays scores)
- Collision detection (ball vs. paddle, ball vs. walls)
- Event handling with `screen.onkeypress()` for fluid paddle movement
- Game loop control with `screen.update()` and `time.sleep()`
- Writing modular Python code (separate files for `main.py`, `paddle.py`, `ball.py`, `scoreboard.py`)

---

## ⌨️ Controls
- **Left Paddle:** `W` (up), `S` (down)  
- **Right Paddle:** `↑` (up), `↓` (down)

---

## 🚀 How to Run
1. Clone the repo:
   ```bash
   git clone https://github.com/martialchess/pong-game.git
2. Run the game:
   python main.py

   
