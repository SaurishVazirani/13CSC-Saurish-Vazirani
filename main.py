from tkinter import *

import ImageTk

window = Tk()
window.geometry("420x420")
window.title("RepFit")

import tkinter as tk
from PIL import Image

root = tk.Tk()

image_filename = "Dumbell.png"

load = Image.open('Images/Dumbell.png')

img = Image.open('Images/Dumbell.png')
render = ImageTk.PhotoImage(load)

img_label = tk.Label(root, Image=render)
img_label.pack()

root.mainloop()

window.config(background="#99c5ff")

label_title = Label(window,
                    text="RepFit",
                    font=('Arial',200,'bold'),
                    fg='black',
                    bg='#99c5ff',
                    compound='left')

label_title.pack()
label_sub = Label(window,text="Progress, Not Perfection",font=('Arial', 50,'normal'),fg='black', bg='#99c5ff')
label_sub.place(x=0,y=80)
label_sub.pack()
