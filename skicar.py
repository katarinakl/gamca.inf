import tkinter
from random import randrange, randint

X_MAX,Y_MAX= 800,600
canvas=tkinter.Canvas(width=X_MAX,height=Y_MAX,background="white")
canvas.pack()

x1,y1=0,0

hrubka=2
farba="black"

def klik(event):
    global x1,y1
    canvas.bind("<B1-Motion>",ciara)
    x1,y1=event.x,event.y

    x,y=event.x,event.y
    global farba, hrubka
    if  y >= 500 and x >= 700:
        farba="blue"
    elif y >= 500 and 700> x >= 600:
        farba="green"
    elif y >= 500 and 600 > x >= 500:
        farba="red"
    elif y >= 500 and 500 > x >= 400:
        farba="black"
    else:
        pass

    if  y >= 500 and 100 > x:
        hrubka=2
    elif y >= 500 and 200 > x >= 100:
        hrubka=6
    elif y >= 500 and 300 > x >= 200:
        hrubka=10
    else:
        pass

    if 200 > x and 100 > y:
        canvas.delete("all")
        moznosti()

    print(hrubka)
    print(farba)

def moznosti():
    canvas.create_rectangle(0,0,200,100,outline="black")
    canvas.create_text(100,50,fill="black",font="Ariel",text="DELETE")
    canvas.create_rectangle(0,500,100,600,outline="black")
    canvas.create_oval(40,540,60,560,fill="black")
    canvas.create_rectangle(100,500,200,600,outline="black")
    canvas.create_oval(130,530,170,570,fill="black")
    canvas.create_rectangle(200,500,300,600,outline="black")
    canvas.create_oval(220,520,280,580,fill="black")
    canvas.create_rectangle(400,500,500,600,outline="black",fill="black")
    canvas.create_rectangle(500,500,600,600,outline="black",fill="red")
    canvas.create_rectangle(600,500,700,600,outline="black",fill="green")
    canvas.create_rectangle(700,500,800,600,outline="black",fill="blue")

def ciara(event):
    x,y=event.x,event.y
    global x1,y1
    canvas.create_line(x1,y1,x,y,width=hrubka,fill=farba)
    x1,y1=x,y

canvas.bind("<Button-1>", klik)
moznosti()
