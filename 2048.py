import tkinter as tk
import random

class Game(tk.Frame):
    # Making Color
    Color_grid = "#b8afa9"
    Color_EmptyCell = "#ffd5b5"
    Font_ScoreLabel = ("Verdana", 24)
    Font_Score = ("Helvetica", 48, "bold")
    Font_GameOver = ("Helvetica", 48, "bold")
    Font_Color_GameOver = "#ffffff"
    Winner_BG = "#ffcc00"
    Loser_BG = "#a39489"

    Color_Cells = {
        2: "#fcefe6",
        4: "#f2e8cb",
        8: "#f5b682",
        16: "#f29446",
        32: "#ff775c",
        64: "#e64c2e",
        128: "#ede291",
        256: "#fce130",
        512: "#ffdb4a",
        1024: "#f0b922",
        2048: "#fad74d"
    }

    Color_CellNumber = {
        2: "#695c57",
        4: "#695c57",
        8: "#ffffff",
        16: "#ffffff",
        32: "#ffffff",
        64: "#ffffff",
        128: "#ffffff",
        256: "#ffffff",
        512: "#ffffff",
        12048: "#ffffff"
    }

    Fonts_CellNumebr = {
        2: ("Helvetica", 55, "bold"),
        4: ("Helvetica", 55, "bold"),
        8: ("Helvetica", 55, "bold"),
        16: ("Helvetica", 50, "bold"),
        32: ("Helvetica", 50, "bold"),
        64: ("Helvetica", 50, "bold"),
        128: ("Helvetica", 45, "bold"),
        256: ("Helvetica", 45, "bold"),
        512: ("Helvetica", 45, "bold"),
        1024: ("Helvetica", 40, "bold"),
        2048: ("Helvetica", 40, "bold"),
    }

    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.master.title("2048")

        self.grid_main = tk.Frame(
            self, bg=Game.Color_grid, bd=3, width=400, height=400
        )
        self.grid_main.grid(pady=(110, 0))

        self.game_over_frame = None  # Track the game over frame
        self.GUI_maker()
        self.start_game()

        self.master.bind("<Left>", self.left)
        self.master.bind("<Right>", self.right)
        self.master.bind("<Up>", self.up)
        self.master.bind("<Down>", self.down)

        self.mainloop()

    # Create a function to make GUI
    def GUI_maker(self):
        # Make grid
        self.cells = []
        for i in range(4):
            row = []
            for j in range(4):
                frame_cells = tk.Frame(
                    self.grid_main,
                    bg=Game.Color_EmptyCell,
                    width=100,
                    height=100
                )
                frame_cells.grid(row=i, column=j, padx=5, pady=5)
                cell_number = tk.Label(self.grid_main, bg=Game.Color_EmptyCell)
                cell_data = {"frame": frame_cells, "number": cell_number}

                cell_number.grid(row=i, column=j)
                row.append(cell_data)
            self.cells.append(row)

        # Creating Score header
        frame_score = tk.Frame(self)
        frame_score.place(relx=0.5, y=45, anchor="center")
        tk.Label(
            frame_score,
            text="Score",
            font=Game.Font_ScoreLabel
        ).grid(row=0)
        self.label_score = tk.Label(frame_score, text="0", font=Game.Font_Score)
        self.label_score.grid(row=1)

        # Creating Reset button
        reset_button = tk.Button(
            self,
            text="Reset",
            command=self.reset_game,
            font=Game.Font_ScoreLabel
        )
        reset_button.place(relx=1.0, rely=0.0, anchor="ne")

    # Create a function to start the game
    def start_game(self):
        # Create a matrix of zeroes
        self.matrix = [[0] * 4 for _ in range(4)]

        # Fill 2 random cells with 2s
        for _ in range(2):
            row = random.randint(0, 3)
            col = random.randint(0, 3)
            while self.matrix[row][col] != 0:
                row = random.randint(0, 3)
                col = random.randint(0, 3)
            self.matrix[row][col] = 2

        self.score = 0

    # Make matrix manipulation functions
    def stack(self):
        Matrix_1 = [[0] * 4 for _ in range(4)]
        for i in range(4):
            position_fill = 0
            for j in range(4):
                if self.matrix[i][j] != 0:
                    Matrix_1[i][position_fill] = self.matrix[i][j]
                    position_fill += 1
        self.matrix = Matrix_1

    def combine(self):
        for i in range(4):
            for j in range(3):
                if self.matrix[i][j] != 0 and self.matrix[i][j] == self.matrix[i][j + 1]:
                    self.matrix[i][j] *= 2
                    self.matrix[i][j + 1] = 0
                    self.score += self.matrix[i][j]

    def reverse(self):
        Matrix_1 = []
        for i in range(4):
            Matrix_1.append([])
            for j in range(4):
                Matrix_1[i].append(self.matrix[i][3 - j])
        self.matrix = Matrix_1

    def transpose(self):
        Matrix_1 = [[0] * 4 for _ in range(4)]
        for i in range(4):
            for j in range(4):
                Matrix_1[i][j] = self.matrix[j][i]
        self.matrix = Matrix_1

    # Create a function to randomly add a new 2 or 4 tile to an empty cell
    def add_tile(self):
        empty_cells = []
        for i in range(4):
            for j in range(4):
                if self.matrix[i][j] == 0:
                    empty_cells.append((i, j))
        if empty_cells:
            row, col = random.choice(empty_cells)
            self.matrix[row][col] = random.choice([2, 4])

    # Create a function to update GUI to match the matrix
    def GUI_update(self):
        for i in range(4):
            for j in range(4):
                cell_value = self.matrix[i][j]
                if cell_value == 0:
                    self.cells[i][j]["frame"].configure(bg=Game.Color_EmptyCell)
                    self.cells[i][j]["number"].configure(bg=Game.Color_EmptyCell, text="")
                else:
                    self.cells[i][j]["frame"].configure(bg=Game.Color_Cells[cell_value])
                    self.cells[i][j]["number"].configure(
                        bg=Game.Color_Cells[cell_value],
                        fg=Game.Color_CellNumber[cell_value],
                        font=Game.Fonts_CellNumebr[cell_value],
                        text=str(cell_value)
                    )
        self.label_score.configure(text=self.score)
        self.update_idletasks()

    # Create a function for pressing arrow buttons to play the game
    def left(self, event):
        self.stack()
        self.combine()
        self.stack()
        self.add_tile()
        self.GUI_update()
        self.game_over()

    def right(self, event):
        self.reverse()
        self.stack()
        self.combine()
        self.stack()
        self.reverse()
        self.add_tile()
        self.GUI_update()
        self.game_over()

    def up(self, event):
        self.transpose()
        self.stack()
        self.combine()
        self.stack()
        self.transpose()
        self.add_tile()
        self.GUI_update()
        self.game_over()

    def down(self, event):
        self.transpose()
        self.reverse()
        self.stack()
        self.combine()
        self.stack()
        self.reverse()
        self.transpose()
        self.add_tile()
        self.GUI_update()
        self.game_over()

    # Check if any moves are possible
    def exists_horizontal_moves(self):
        for i in range(4):
            for j in range(3):
                if self.matrix[i][j] == self.matrix[i][j + 1]:
                    return True
        return False

    def exists_vertical_moves(self):
        for i in range(3):
            for j in range(4):
                if self.matrix[i][j] == self.matrix[i + 1][j]:
                    return True
        return False

    # Check if the game is over (Win/Lose)
    def game_over(self):
        if any(2048 in row for row in self.matrix):
            game_over_frame = tk.Frame(self.grid_main, borderwidth=2)
            game_over_frame.place(relx=0.5, rely=0.5, anchor="center")
            tk.Label(
                game_over_frame,
                text="YOU WIN!!",
                bg=Game.Winner_BG,
                fg=Game.Font_Color_GameOver,
                font=Game.Font_GameOver
            ).pack()
        elif not any(0 in row for row in self.matrix) and not self.exists_horizontal_moves() and not self.exists_vertical_moves():
            game_over_frame = tk.Frame(self.grid_main, borderwidth=2)
            game_over_frame.place(relx=0.5, rely=0.5, anchor="center")
            tk.Label(
                game_over_frame,
                text="GAME OVER!!",
                bg=Game.Loser_BG,
                fg=Game.Font_Color_GameOver,
                font=Game.Font_GameOver
            ).pack()

    # Create a function to reset the game
    def reset_game(self):
        self.start_game()
        self.GUI_update()


game = Game()
