from tkinter import *
root=Tk()

frameTop=Frame(root)
frameTop.pack()
frameBottom=Frame(root)
frameBottom.pack()

button1=Button(frameTop,text="Button1",fg="red")
button2=Button(frameTop,text="Button2",fg="yellow")
button3=Button(frameTop,text="Button3",fg="green")

button4=Button(frameBottom,text="Button4",fg="cyan")
button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)

button4.pack(side=BOTTOM)








root.mainloop()