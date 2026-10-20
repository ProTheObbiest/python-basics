from tkinter import *

root = Tk()
canvas = Canvas(root, width=600, height=400, bg="white")
canvas.pack()

def draw_circle(canvas, x, y, radius, color):
    x1 = x
    y1 = y
    x2 = x1+radius
    y2 = y1+radius
    canvas.create_oval(x1, y1, x2, y2, fill=color)

circle_x = 15
circle_y = 15
circle_radius = 25

for i in range(10):
    draw_circle(canvas, circle_x, circle_y, circle_radius, "black")
    circle_x += circle_radius+5
    circle_y += circle_radius-11
    circle_radius += 5

root.mainloop()