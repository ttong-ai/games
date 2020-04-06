import tkinter as tk

window = tk.Tk()
window.title("Nathan's Chessboard")
window.geometry("450x600")

canvases = []
for r in range(8):
    for c in range(8):
        if (r + c) % 2 == 0:
            color = "black"
        else:
            color = "white"
        this_canvas = tk.Canvas(window, width=50, height=50, background=color, border=0)
        this_canvas.grid(row=r, column=c, padx=0, pady=0)
        canvases.append(this_canvas)

# label = tk.Label(text="click me!")
# label.grid(row=8, column=0)

window.mainloop()
