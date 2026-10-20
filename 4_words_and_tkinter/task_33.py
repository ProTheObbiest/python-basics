from tkinter import *

root = Tk()
canvas = Canvas(root, width=490, height=60, bg="white")
canvas.pack()

size = 40
distance = 10

for i in range(10):
    x1 = i * (size + distance)
    y1 = 10
    x2 = x1 + size
    y2 = y1 + size

    color = "red" if i % 2 == 0 else "blue"

    canvas.create_rectangle(x1, y1, x2, y2, fill=color)

root.mainloop()