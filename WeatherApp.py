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
frame = tk.Frame(root, bg='lightgreen', bd=3)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')
# relative x and relative y to center the frame, anchor='n' to set it in the middle

entry = tk.Entry(frame, bg='lightgray', font=40)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get weather", bg='crimson')
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg='lightgreen', bd=6)  # create another frame
lower_frame.place(relx=0.5, rely=0.25, relheight=0.6,
                  relwidth=0.75, anchor='n')

label = tk.Label(lower_frame)
label.place(relwidth=1, relheight=1)

root.mainloop()
# Anything that we put in the app will be run between these two lines of code
