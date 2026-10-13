# 🎮 College Tic-Tac-Toe Python Desktop Game

A complete, beginner-friendly desktop Tic-Tac-Toe project developed in **Python** using the standard **Tkinter** graphical library.

This project was built to fulfill college assignment requirements, featuring clean, well-commented code, modern UI styling, and two distinct computer difficulty modes.

---

## 📁 Files Included

| File | Description |
| :--- | :--- |
| **`random_tictactoe.py`** | **Random Mode**: The computer chooses a random empty square. Casual, fun, and easy to beat. |
| **`intelligent_tictactoe.py`** | **Intelligent AI Mode**: The computer tries to win immediately, blocks your winning moves, and uses the Minimax algorithm. |
| **`README.md`** | Complete guide, instructions for Mac/Windows, and code explanations for your assignment. |

---

## ✨ Features Built Into Both Games

- 🎯 **Clickable 3x3 Board**: Interactive grid with clear turn response.
- ❌ **X for Player, ⭕ O for Computer**: You always move first as `X`.
- 🛡️ **Move Validation**: Already occupied squares cannot be clicked.
- 🏆 **Smart Win Detection**: Checks all rows, columns, and diagonals. Highlights the 3 winning squares in vibrant green!
- 🤝 **Draw Detection**: Detects when all 9 squares are full with no winner.
- 📊 **Live Scoreboard**: Tracks Player Wins, Computer Wins, and Draws across rounds.
- 🔄 **Restart Round Button**: Clears the board for another game while preserving your scores.
- 🧹 **Reset Scores Button**: Resets all scores back to 0.
- 🎨 **Modern Dark Theme**: Designed with a sleek palette (Slate 900, Cyan, Amber, Emerald Green).

---

## 🍎 How to Run on Mac (Step-by-Step for Beginners)

Running Python desktop games on a Mac is very easy. Follow these simple steps:

### Step 1: Open the Terminal
1. Press `Command (⌘) + Space` on your keyboard to open Spotlight Search.
2. Type `Terminal` and press **Enter**.

### Step 2: Verify Python 3 is Installed
In your Terminal window, type:
```bash
python3 --version
```
Press **Enter**. You should see something like `Python 3.10.x`, `Python 3.11.x`, or `Python 3.12.x`.
*(If not installed, download the official installer from [python.org](https://www.python.org/downloads/mac-osx/)).*

### Step 3: Navigate to Your Project Folder
Type `cd` followed by a space, and then type the path to your folder.
For example, if your folder is on your Desktop:
```bash
cd ~/Desktop/"tic tac toe"
```
*(Tip: You can also type `cd ` and drag-and-drop the folder from Finder directly into the Terminal window!)*

### Step 4: Run the Games!

- **To run Random Mode:**
  ```bash
  python3 random_tictactoe.py
  ```

- **To run Intelligent AI Mode:**
  ```bash
  python3 intelligent_tictactoe.py
  ```

The game window will immediately open on your screen!

> **Note for Mac users**: macOS comes with `tkinter` pre-installed with official Python from python.org. If you use Homebrew and encounter a `No module named '_tkinter'` message, simply run:
> ```bash
> brew install python-tk
> ```

---

## 🪟 How to Run on Windows (Alternative)

If you are running on Windows:
1. Open **Command Prompt** or **PowerShell**.
2. Navigate to your project folder:
   ```cmd
   cd "C:\Users\ajaym\OneDrive\Desktop\tic tac toe"
   ```
3. Run either file:
   ```cmd
   python random_tictactoe.py
   python intelligent_tictactoe.py
   ```
4. *(Or simply double-click either `.py` file in File Explorer!)*

---

## 🧠 How the AI Works (Explained Simply for College)

### 1. Random Mode (`random_tictactoe.py`)
1. The game scans the board and finds all coordinates `(row, col)` where the cell is empty (`" "`).
2. It uses Python's built-in `random.choice(empty_cells)` to pick one at random.
3. It places `"O"` there.

### 2. Intelligent Mode (`intelligent_tictactoe.py`)
The intelligent computer plays strategically in three clear steps:

```
                  ┌──────────────────────────────────────────────┐
                  │ Does the Computer ('O') have a WINNING move? │
                  └──────────────────────┬───────────────────────┘
                                         │
                         YES ────────────┴──────────── NO
                          │                            │
                          ▼                            ▼
                 [ Take Winning Move! ]  ┌──────────────────────────────────────────────┐
                                         │  Is the Player ('X') about to WIN this turn? │
                                         └──────────────────────┬───────────────────────┘
                                                                │
                                                YES ────────────┴──────────── NO
                                                 │                            │
                                                 ▼                            ▼
                                        [ Block Player's Move! ]     [ Use Minimax / Optimal ]
```

1. **Step 1 — WIN**: The computer simulates placing `"O"` in every empty square. If any square creates 3-in-a-row for `"O"`, it immediately plays there to win the game!
2. **Step 2 — BLOCK**: If it cannot win immediately, it simulates placing `"X"` in every empty square. If the human player could win on their next turn, the computer immediately places `"O"` there to block them!
3. **Step 3 — MINIMAX**: If no immediate win or block exists, the computer uses the **Minimax Algorithm** (a standard Artificial Intelligence search algorithm) to evaluate all possible future moves. It awards `+10` for wins, `-10` for losses, and `0` for ties, choosing the move that guarantees the best possible outcome.

---

## 🎓 College Viva / Presentation Q&A

Here are common questions professors ask about this assignment, along with simple answers:

**Q1: What library did you use for the GUI?**
> *"I used Tkinter, which is the standard, built-in Graphical User Interface library included with Python. It requires no third-party package installations and works across Mac, Windows, and Linux."*

**Q2: How is the board state stored in memory?**
> *"The board is represented as a 2D list of 3 rows and 3 columns: `board[row][col]`. Empty squares contain `" "`, the player is `"X"`, and the computer is `"O"`."*

**Q3: How does the game detect a win?**
> *"The function `check_winner()` checks all 8 possible winning lines: the 3 horizontal rows, the 3 vertical columns, and both diagonals (main diagonal and anti-diagonal). When 3 matching non-empty symbols are found, it returns the winner and highlights those three squares."*

**Q4: How does the computer prevent playing in an occupied square?**
> *"Before making any move, the code checks `if self.board[row][col] != ' '`. If the cell is already occupied, the move is rejected."*

**Q5: What makes the Intelligent AI different from the Random mode?**
> *"The Random mode selects any open square using `random.choice()`. The Intelligent mode first checks for an immediate win, then checks if it needs to block the player's winning move, and finally applies the Minimax algorithm to choose optimal positioning."*

---

## 📜 License
This project is prepared for educational and college assignment purposes. Feel free to modify and adapt it!
