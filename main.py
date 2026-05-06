from tkinter import *

window = Tk()
window.geometry("420x420")
window.title("RepFit")

window.config(background="#99c5ff")

photo=PhotoImage(file='C:\\Users\\24223\\Downloads\\Dumbell.png')

label = Label(window,text="RepFit",font=('Arial',200,'bold'),fg='black',bg='#99c5ff')
label.pack()
label = Label(window,text="Progress, Not Perfection",font=('Arial', 50,'normal'),fg='black', bg='#99c5ff')
label.place(x=0,y=80)
label.pack()
label = Label(window, image=photo, bg='#99c5ff')
label.place(x=100,y=100)
label.pack()
window.mainloop()

