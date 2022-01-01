import tkinter as tk
from typing import Text

HEIGHT = 700
WIDTH = 700

# Anything that we put in the app will be run between these two lines of code
root = tk.Tk()

# 5th, we created a canva that'll be in the root
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

# 6th, a frame inside the canva
frame = tk.Frame(root, bg='darkgreen')
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
# relative x and relative y to center the frame

button = tk.Button(frame, text="Test Button", bg='crimson')  # Creating button
# That will put the button on the screen inside the frame
button.place(relx=0, rely=0, relheight=0.25, relwidth=0.25)

# 7th, label and entry
label = tk.Label(frame, text="I'm a label", bg='lightyellow')
label.pack(side='right', fill='y')

entry = tk.Entry(frame, bg='lightgray')  # entry is where you type an input
entry.pack(side='right', fill='y')  # change position and size by pack
# can use .grid() or .place() instead

root.mainloop()
# Anything that we put in the app will be run between these two lines of code
