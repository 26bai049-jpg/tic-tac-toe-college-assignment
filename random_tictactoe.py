"""
=============================================================================
TIC-TAC-TOE : RANDOM MODE
=============================================================================
A modern Python desktop Tic-Tac-Toe game created with Tkinter.

HOW IT WORKS:
- You play as "X" and always move first.
- The computer plays as "O" and chooses a RANDOM empty square.
- First to get 3 in a row (horizontal, vertical, or diagonal) wins!
- Scoreboard tracks Player wins, Computer wins, and Ties.

Designed for college assignments: Simple, beginner-friendly, and well-commented.
=============================================================================
"""

import tkinter as tk
from tkinter import font as tkfont
import random


class RandomTicTacToe:
    """
    Main application class for the Random Mode Tic-Tac-Toe game.
    Manages the graphical interface, game board, moves, and win checking.
    """

    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe — Random Mode")
        self.root.resizable(False, False)

        # -------------------------------------------------------------------
        # COLOR PALETTE (Modern Dark Theme)
        # -------------------------------------------------------------------
        self.BG_MAIN = "#0f172a"       # Deep Slate background
        self.BG_CARD = "#1e293b"       # Card / container background
        self.BG_BUTTON = "#334155"     # Default grid tile color
        self.BG_HOVER = "#475569"      # Tile hover color
        self.BG_WIN = "#16a34a"        # Vibrant green for winning line
        self.COLOR_X = "#38bdf8"       # Electric cyan for Player (X)
        self.COLOR_O = "#fb923c"       # Warm amber for Computer (O)
        self.TEXT_MAIN = "#f8fafc"     # Primary white text
        self.TEXT_MUTED = "#94a3b8"    # Secondary gray text
        self.BTN_PRIMARY = "#2563eb"   # Primary blue for Restart button
        self.BTN_SECONDARY = "#475569" # Gray for Reset Score button

        self.root.configure(bg=self.BG_MAIN)

        # -------------------------------------------------------------------
        # GAME STATE VARIABLES
        # -------------------------------------------------------------------
        # 3x3 grid represented as a 2D list of strings (" " = empty, "X", "O")
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        
        # Flags to control turns and prevent accidental clicks
        self.game_over = False
        self.waiting_for_computer = False

        # Score counters across multiple rounds
        self.player_score = 0
        self.computer_score = 0
        self.draws_score = 0

        # 2D list to store the 3x3 Tkinter button objects
        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        # -------------------------------------------------------------------
        # BUILD THE USER INTERFACE
        # -------------------------------------------------------------------
        self.create_widgets()
        self.center_window(430, 610)

    # =======================================================================
    # UI SETUP
    # =======================================================================

    def center_window(self, width, height):
        """Centers the game window on the user's screen."""
        self.root.update_idletasks()
        screen_w = self.root.winfo_screenwidth()
        screen_h = self.root.winfo_screenheight()
        x = max(0, (screen_w - width) // 2)
        y = max(0, (screen_h - height) // 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")

    def create_widgets(self):
        """Creates and organizes all labels, scoreboards, tiles, and buttons."""
        
        # 1. Header Frame (Title and Subtitle)
        header_frame = tk.Frame(self.root, bg=self.BG_MAIN)
        header_frame.pack(pady=(18, 6))

        title_label = tk.Label(
            header_frame,
            text="TIC-TAC-TOE",
            font=("Helvetica", 20, "bold"),
            fg=self.TEXT_MAIN,
            bg=self.BG_MAIN
        )
        title_label.pack()

        mode_badge = tk.Label(
            header_frame,
            text="🎲 MODE: RANDOM COMPUTER",
            font=("Helvetica", 9, "bold"),
            fg="#a855f7",               # Purple accent badge
            bg=self.BG_MAIN
        )
        mode_badge.pack(pady=(2, 0))

        # 2. Scoreboard Frame
        score_frame = tk.Frame(self.root, bg=self.BG_CARD, padx=14, pady=8, relief="ridge", bd=1)
        score_frame.pack(padx=20, pady=8, fill="x")

        # Column configuration for uniform spacing
        score_frame.columnconfigure(0, weight=1)
        score_frame.columnconfigure(1, weight=1)
        score_frame.columnconfigure(2, weight=1)

        # Player (X) score
        self.lbl_p_name = tk.Label(score_frame, text="YOU (X)", font=("Helvetica", 9, "bold"), fg=self.COLOR_X, bg=self.BG_CARD)
        self.lbl_p_name.grid(row=0, column=0)
        self.lbl_p_score = tk.Label(score_frame, text="0", font=("Helvetica", 16, "bold"), fg=self.TEXT_MAIN, bg=self.BG_CARD)
        self.lbl_p_score.grid(row=1, column=0)

        # Draws score
        self.lbl_d_name = tk.Label(score_frame, text="DRAWS", font=("Helvetica", 9, "bold"), fg=self.TEXT_MUTED, bg=self.BG_CARD)
        self.lbl_d_name.grid(row=0, column=1)
        self.lbl_d_score = tk.Label(score_frame, text="0", font=("Helvetica", 16, "bold"), fg=self.TEXT_MAIN, bg=self.BG_CARD)
        self.lbl_d_score.grid(row=1, column=1)

        # Computer (O) score
        self.lbl_c_name = tk.Label(score_frame, text="AI (O)", font=("Helvetica", 9, "bold"), fg=self.COLOR_O, bg=self.BG_CARD)
        self.lbl_c_name.grid(row=0, column=2)
        self.lbl_c_score = tk.Label(score_frame, text="0", font=("Helvetica", 16, "bold"), fg=self.TEXT_MAIN, bg=self.BG_CARD)
        self.lbl_c_score.grid(row=1, column=2)

        # 3. Status Banner (Instructions & turn indicators)
        self.status_label = tk.Label(
            self.root,
            text="Your turn! Click any empty square (X)",
            font=("Helvetica", 11, "bold"),
            fg=self.COLOR_X,
            bg=self.BG_MAIN
        )
        self.status_label.pack(pady=(4, 10))

        # 4. 3x3 Game Board Grid Frame
        board_container = tk.Frame(self.root, bg=self.BG_CARD, padx=8, pady=8, relief="flat", bd=0)
        board_container.pack(padx=20, pady=2)

        for r in range(3):
            for c in range(3):
                btn = tk.Button(
                    board_container,
                    text="",
                    font=("Helvetica", 24, "bold"),
                    width=4,
                    height=2,
                    bg=self.BG_BUTTON,
                    fg=self.TEXT_MAIN,
                    activebackground=self.BG_HOVER,
                    activeforeground=self.TEXT_MAIN,
                    highlightbackground=self.BG_CARD,
                    relief="flat",
                    bd=0,
                    cursor="hand2",
                    command=lambda row=r, col=c: self.on_cell_click(row, col)
                )
                btn.grid(row=r, column=c, padx=4, pady=4)
                self.buttons[r][c] = btn

        # 5. Bottom Controls (Restart Game & Reset Score)
        controls_frame = tk.Frame(self.root, bg=self.BG_MAIN)
        controls_frame.pack(pady=(16, 12))

        self.btn_restart = tk.Button(
            controls_frame,
            text="🔄 Restart Round",
            font=("Helvetica", 11, "bold"),
            bg=self.BTN_PRIMARY,
            fg="#ffffff",
            activebackground="#1d4ed8",
            activeforeground="#ffffff",
            highlightbackground=self.BG_MAIN,
            relief="flat",
            padx=14,
            pady=6,
            cursor="hand2",
            command=self.restart_game
        )
        self.btn_restart.pack(side="left", padx=6)

        self.btn_reset_score = tk.Button(
            controls_frame,
            text="Reset Scores",
            font=("Helvetica", 10),
            bg=self.BTN_SECONDARY,
            fg="#ffffff",
            activebackground="#334155",
            activeforeground="#ffffff",
            highlightbackground=self.BG_MAIN,
            relief="flat",
            padx=10,
            pady=6,
            cursor="hand2",
            command=self.reset_scores
        )
        self.btn_reset_score.pack(side="left", padx=6)

    # =======================================================================
    # GAMEPLAY LOGIC
    # =======================================================================

    def on_cell_click(self, row, col):
        """
        Triggered whenever the human player clicks on a grid tile.
        Validates the move, updates the board, and triggers the computer's turn.
        """
        # Rule 1: Ignore click if the game is already finished
        if self.game_over:
            return

        # Rule 2: Ignore click if it is the computer's turn
        if self.waiting_for_computer:
            return

        # Rule 3: Do not allow moves in already occupied squares
        if self.board[row][col] != " ":
            self.status_label.config(
                text="⚠️ Square already occupied! Choose an empty one.",
                fg="#facc15"
            )
            return

        # --- PLAYER'S MOVE ---
        self.board[row][col] = "X"
        self.update_button_visual(row, col, "X")

        # Check if Player won
        winner, win_line = self.check_winner()
        if winner == "X":
            self.handle_win("X", win_line)
            return

        # Check if the board is full (Draw)
        if self.is_board_full():
            self.handle_draw()
            return

        # --- PREPARE FOR COMPUTER'S MOVE ---
        self.waiting_for_computer = True
        self.status_label.config(
            text="Computer is thinking... 🤖",
            fg=self.COLOR_O
        )

        # Add a realistic 400ms delay so the player sees their move first
        self.root.after(400, self.computer_move)

    def computer_move(self):
        """
        Executes the computer's move using RANDOM mode:
        1. Gathers all empty squares.
        2. Randomly selects one empty square.
        3. Places 'O' and checks for win or draw.
        """
        if self.game_over:
            return

        # Find all empty squares on the 3x3 board
        empty_cells = []
        for r in range(3):
            for c in range(3):
                if self.board[r][c] == " ":
                    empty_cells.append((r, c))

        # If there are empty cells available, pick one at random
        if empty_cells:
            chosen_row, chosen_col = random.choice(empty_cells)
            self.board[chosen_row][chosen_col] = "O"
            self.update_button_visual(chosen_row, chosen_col, "O")

            # Check if Computer won
            winner, win_line = self.check_winner()
            if winner == "O":
                self.handle_win("O", win_line)
                return

            # Check for a draw
            if self.is_board_full():
                self.handle_draw()
                return

        # Hand control back to the human player
        self.waiting_for_computer = False
        self.status_label.config(
            text="Your turn! Click any empty square (X)",
            fg=self.COLOR_X
        )

    # =======================================================================
    # WIN & DRAW DETECTION
    # =======================================================================

    def check_winner(self):
        """
        Examines all 8 possible winning lines:
        - 3 horizontal rows
        - 3 vertical columns
        - 2 diagonals

        Returns:
            (winner_symbol, list_of_winning_coordinates) if someone won,
            (None, None) otherwise.
        """
        # 1. Check Rows
        for r in range(3):
            if self.board[r][0] != " " and self.board[r][0] == self.board[r][1] == self.board[r][2]:
                return self.board[r][0], [(r, 0), (r, 1), (r, 2)]

        # 2. Check Columns
        for c in range(3):
            if self.board[0][c] != " " and self.board[0][c] == self.board[1][c] == self.board[2][c]:
                return self.board[0][c], [(0, c), (1, c), (2, c)]

        # 3. Check Main Diagonal (Top-Left to Bottom-Right)
        if self.board[0][0] != " " and self.board[0][0] == self.board[1][1] == self.board[2][2]:
            return self.board[0][0], [(0, 0), (1, 1), (2, 2)]

        # 4. Check Anti-Diagonal (Top-Right to Bottom-Left)
        if self.board[0][2] != " " and self.board[0][2] == self.board[1][1] == self.board[2][0]:
            return self.board[0][2], [(0, 2), (1, 1), (2, 0)]

        return None, None

    def is_board_full(self):
        """Returns True if every cell on the board contains 'X' or 'O'."""
        for r in range(3):
            for c in range(3):
                if self.board[r][c] == " ":
                    return False
        return True

    # =======================================================================
    # OUTCOME HANDLERS
    # =======================================================================

    def handle_win(self, winner, winning_line):
        """Updates score, highlights the winning tiles, and shows message."""
        self.game_over = True
        self.waiting_for_computer = False

        # Highlight the 3 winning squares in vibrant green
        for r, c in winning_line:
            self.buttons[r][c].config(
                bg=self.BG_WIN,
                fg="#ffffff",
                activebackground=self.BG_WIN,
                activeforeground="#ffffff"
            )

        if winner == "X":
            self.player_score += 1
            self.lbl_p_score.config(text=str(self.player_score))
            self.status_label.config(
                text="🎉 You Won! Congratulations!",
                fg="#22c55e"
            )
        else:
            self.computer_score += 1
            self.lbl_c_score.config(text=str(self.computer_score))
            self.status_label.config(
                text="🤖 Computer Won! Better luck next round!",
                fg="#ef4444"
            )

    def handle_draw(self):
        """Updates draw score and displays a tie message."""
        self.game_over = True
        self.waiting_for_computer = False
        self.draws_score += 1
        self.lbl_d_score.config(text=str(self.draws_score))
        self.status_label.config(
            text="🤝 It's a Draw! Well played.",
            fg="#eab308"
        )

    def update_button_visual(self, row, col, symbol):
        """Updates the text and styling of a specific board button."""
        color = self.COLOR_X if symbol == "X" else self.COLOR_O
        self.buttons[row][col].config(
            text=symbol,
            fg=color,
            activeforeground=color
        )

    # =======================================================================
    # RESET & RESTART METHODS
    # =======================================================================

    def restart_game(self):
        """Resets the 3x3 board for a new round while preserving scores."""
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.game_over = False
        self.waiting_for_computer = False

        for r in range(3):
            for c in range(3):
                self.buttons[r][c].config(
                    text="",
                    bg=self.BG_BUTTON,
                    fg=self.TEXT_MAIN,
                    activebackground=self.BG_HOVER,
                    activeforeground=self.TEXT_MAIN
                )

        self.status_label.config(
            text="Your turn! Click any empty square (X)",
            fg=self.COLOR_X
        )

    def reset_scores(self):
        """Resets the scoreboard counters to 0 and starts a fresh game."""
        self.player_score = 0
        self.computer_score = 0
        self.draws_score = 0
        self.lbl_p_score.config(text="0")
        self.lbl_c_score.config(text="0")
        self.lbl_d_score.config(text="0")
        self.restart_game()


# ===========================================================================
# PROGRAM ENTRY POINT
# ===========================================================================
if __name__ == "__main__":
    app_root = tk.Tk()
    game = RandomTicTacToe(app_root)
    app_root.mainloop()
