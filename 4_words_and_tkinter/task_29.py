from tkinter import *

root = Tk()
canvas = Canvas(root, width=600, height=300)
canvas.pack()

width = 600
height = 300
stripe_height = height / 3

canvas.create_rectangle(0, 0, width, stripe_height, fill="blue", outline="blue")

canvas.create_rectangle(0, stripe_height, width, stripe_height * 2, fill="black", outline="black")

canvas.create_rectangle(0, stripe_height * 2, width, height, fill="white", outline="white")

root.mainloop()