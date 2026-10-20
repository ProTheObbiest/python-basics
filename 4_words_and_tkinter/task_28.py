from tkinter import *

root = Tk()
canvas = Canvas(root, width=600, height=400, bg="white")
canvas.pack()

canvas.create_rectangle(50, 50, 200, 120, fill="red")

canvas.create_oval(250, 50, 350, 150, fill="blue")

canvas.create_line(50, 180, 250, 180, fill="green", width=4)

canvas.create_oval(300, 200, 500, 280, fill="yellow")

canvas.create_text(300, 340, text="My figures", font=("Arial", 18))

root.mainloop()