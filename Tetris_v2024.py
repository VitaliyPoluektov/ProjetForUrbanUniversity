import tkinter as tk

cs = 30
C = 12
R = 20
height = R * cs
width = C * cs

def draw_cell_by_cr(canvas, c, r, color = "#CCCCCC"):
    x0 = c * cs
    y0 = r * cs
    x1 = c * cs + cs
    y1 = r * cs + cs
    canvas.create_rectangle(x0, y0, x1, y1, fill = color, outline = "white", width = 2)

def draw_blank_board(canvas):
    for ri in range(R):
        for ci in range(C):
            draw_cell_by_cr(canvas, ci, ri)

S = {"O": [(-1, -1), (0, -1), (-1, 0), (0, 0)]}
SC = {"O": "blue"}

def draw_cells(canvas, c, r, cell_list, color = "#CCCCCC"):
    for cell in cell_list:
        cell_c, cell_r = cell
        ci = cell_c + c
        ri = cell_r + r
        if 0 <= c < C and 0 <= r < R:
            draw_cell_by_cr(canvas, ci, ri, color)

win = tk.Tk()
canvas = tk.Canvas(win, width = width, height = height)
canvas.pack()

draw_blank_board(canvas)
draw_cells(canvas, 4, 4, S["O"], SC["O"])
win.mainloop()