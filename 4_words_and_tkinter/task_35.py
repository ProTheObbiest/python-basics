from tkinter import *

root = Tk()
canvas = Canvas(root, width=800, height=600, bg="#35558f")
canvas.pack()

# Ночное небо и луна
canvas.create_oval(620, 50, 740, 170, fill="#ffe99a", outline="#ffe99a")

# Высота и ширина зданий
buildings = [
    (20, 300, 140),
    (180, 370, 150),
    (350, 180, 170),
    (540, 330, 140),
    (700, 430, 90)
]

# Рисуем здания и окна
for x, y, width in buildings:
    canvas.create_rectangle(x, y, x + width, 600,
                            fill="#071943", outline="#071943")

    # Окна
    window_size = 20
    gap = 12

    for row in range(y + 20, 570, 45):
        for col in range(x + 15, x + width - 15, 35):
            color = "yellow" if (row + col) % 3 == 0 else "#394e80"

            canvas.create_rectangle(
                col, row,
                col + window_size, row + window_size,
                fill=color, outline=color
            )

# Дверь в одном здании
canvas.create_rectangle(390, 550, 430, 600,
                        fill="#243f70", outline="#243f70")

root.mainloop()