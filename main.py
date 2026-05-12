from tkinter import *

window = Tk()
window.geometry("420x420")
window.title("RepFit")

window.config(background="#99c5ff")

photo = PhotoImage(file='Images/Dumbell.png')

label_title = Label(window,
                    text="RepFit",
                    font=('Arial',200,'bold'),
                    fg='black'
                    ,bg='#99c5ff',
                    compound='left')

label_title.pack()
label_sub = Label(window,text="Progress, Not Perfection",font=('Arial', 50,'normal'),fg='black', bg='#99c5ff')
label_sub.place(x=0,y=80)
label_sub.pack()
label = Label(window, image=photo, bg='#99c5ff',)
label.place(x=0,y=0)
label.pack(pady=(5,20))
label.pack(padx=(10,10))
window.mainloop()

