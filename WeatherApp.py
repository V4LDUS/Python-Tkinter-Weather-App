import tkinter as tk

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
button.pack()  # That will put the button on the screen inside the frame

root.mainloop()
# Anything that we put in the app will be run between these two lines of code
