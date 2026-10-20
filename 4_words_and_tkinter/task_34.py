from tkinter import *

root = Tk()
canvas = Canvas(root, width=500, height=500, bg="white")
canvas.pack()

size = 50
layer = 0

for i in range(8):
    for i in range(8):
        square_i = layer+i
        x1 = (i+1) * size
        y1 = 400-layer*size
        x2 = x1 + size
        y2 = y1 + size
        
        color = "black" if square_i % 2 == 0 else "white"
        
        canvas.create_rectangle(x1, y1, x2, y2, fill=color)
    layer += 1

root.mainloop()