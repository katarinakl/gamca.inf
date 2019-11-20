import tkinter
import random
c=tkinter.Canvas(width=800,height=500,bg="white")
c.pack()

def kvapky():
    for i in range(200):
        x=random.randint(0,790)
        y=random.randint(10,490)
        c.create_oval(x,y,x+10,y+10,fill="light blue")
for i in range (10):
    c.delete("all")
    kvapky()
    c.update()
    c.after(100)
