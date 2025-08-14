import tkinter as tk
from tkinter import messagebox

# ---- Sudoku Solver Logic ----
def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None

def is_valid(board, num, pos):
    row, col = pos

    # Check row
    if num in board[row]:
        return False

    # Check column
    if num in [board[i][col] for i in range(9)]:
        return False

    # Check 3x3 box
    box_x = col // 3
    box_y = row // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num:
                return False

    return True

def solve(board):
    empty_pos = find_empty(board)
    if not empty_pos:
        return True

    row, col = empty_pos
    for num in range(1, 10):
        if is_valid(board, num, (row, col)):
            board[row][col] = num
            if solve(board):
                return True
            board[row][col] = 0  # Backtrack
    return False

# ---- GUI ----
root = tk.Tk()
root.title("Sudoku Solver")

entries = [[None for _ in range(9)] for _ in range(9)]

def get_board():
    board = []
    for i in range(9):
        row = []
        for j in range(9):
            val = entries[i][j].get()
            row.append(int(val) if val.isdigit() else 0)
        board.append(row)
    return board

def display_board(board):
    for i in range(9):
        for j in range(9):
            entries[i][j].delete(0, tk.END)
            entries[i][j].insert(0, str(board[i][j]))

def solve_sudoku():
    board = get_board()
    if solve(board):
        display_board(board)
    else:
        messagebox.showerror("Error", "No solution exists for this Sudoku.")

# Create Entry fields
for i in range(9):
    for j in range(9):
        entry = tk.Entry(root, width=3, font=('Arial', 18), justify='center')
        entry.grid(row=i, column=j, padx=5, pady=5)
        entries[i][j] = entry

# Solve button
tk.Button(root, text="Solve", command=solve_sudoku, font=('Arial', 14), bg='lightgreen').grid(row=9, column=0, columnspan=9, sticky="we")

root.mainloop()
