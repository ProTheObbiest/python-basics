from tkinter import *

root = Tk()
canvas = Canvas(root, width=600, height=400, bg="#DCE9F2", highlightthickness=0)
canvas.pack(fill="both", expand=True)

canvas.create_rectangle(0, 320, 600, 400, fill="#A2C579", outline="")

def draw_wall(canvas, x, y, x_size, y_size, color):
    x1 = x
    y1 = y
    x2 = x1 + x_size
    y2 = y1 + y_size
    canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="")
    
    door_w = x_size * 0.2
    door_h = y_size * 0.35
    door_x = x + (x_size - door_w) / 2
    door_y = y + y_size - door_h
    canvas.create_rectangle(door_x, door_y, door_x + door_w, door_y + door_h, fill="#795548", outline="")

def draw_roof(canvas, x, y, width, height):
    top_x = x + width * 0.5
    top_y = y - height
    left_x = x - width * 0.1
    right_x = x + width * 1.1
    canvas.create_polygon(top_x, top_y, left_x, y, right_x, y, fill="#8D5545", outline="")

def draw_window(canvas, x, y, size):
    x1 = x
    y1 = y
    x2 = x1 + size
    y2 = y1 + size
    canvas.create_rectangle(x1, y1, x2, y2, fill="#EEF6FF", outline="#56748C", width=2)

def draw_house(canvas, x, y, x_size, y_size, color):
    draw_wall(canvas, x, y, x_size, y_size, color)
    draw_roof(canvas, x, y, x_size, y_size * 0.6)
    
    win_size = x_size * 0.22
    win_y = y + y_size * 0.2
    win_x1 = x + x_size * 0.15
    win_x2 = x + x_size * 0.63
    
    draw_window(canvas, win_x1, win_y, win_size)
    draw_window(canvas, win_x2, win_y, win_size)

draw_house(canvas, 40, 200, 120, 120, "#F3C382")
draw_house(canvas, 220, 160, 150, 160, "#E0A0A0")
draw_house(canvas, 440, 220, 100, 100, "#A2B2DB")

root.mainloop()