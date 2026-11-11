import tkinter as tk

width_ = 600
height_ = 400
bg_ = "white"

aken = tk.Tk()
aken.title("Minu esimene graafika")

tahvel = tk.Canvas(
    aken,
    width=width_,
    height=height_,
    bg=bg_)

tahvel.pack()

aken.mainloop()
