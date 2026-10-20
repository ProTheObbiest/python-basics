from tkinter import *

root = Tk()
canvas = Canvas(root, width=500, height=500, bg="white")
canvas.pack()

def draw_square(canvas, x, y, size, color):
    x1 = x
    y1 = y
    x2 = x1 + size
    y2 = y1 + size
                 
    canvas.create_rectangle(x1, y1, x2, y2, fill=color)

draw_square(canvas, 25, 25, 100, "orange")
draw_square(canvas, 150, 25, 50, "yellow")
draw_square(canvas, 225, 25, 150, "blue")
draw_square(canvas, 400, 25, 25, "green")
draw_square(canvas, 150, 200, 40, "purple")

root.mainloop()