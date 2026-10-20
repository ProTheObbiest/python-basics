import tkinter as tk

width_ = int(input("Enter width: "))
height_ = int(input("Enter height: "))
bg_ = input("Enter background color: ")

aken = tk.Tk()
aken.title("Minu esimene graafika")

tahvel = tk.Canvas(
    aken,
    width=width_,
    height=height_,
    bg=bg_)

tahvel.pack()

aken.mainloop()
