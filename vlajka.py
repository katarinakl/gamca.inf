import tkinter
from random import randrange,randint

X_MAX,Y_MAX = 800,600

canvas=tkinter.Canvas(width=X_MAX, height=Y_MAX)
canvas.pack()

x,y = randrange(X_MAX), randrange(Y_MAX)

for i in range (10000):
    x,y = randrange(X_MAX), randrange(Y_MAX)
    if x < 200 and y < 200 or x < 200 and y > 300 or x > 300 and y < 200 or x > 300 and y > 300:
        farba="white"
   
    else:
        farba="blue"

    canvas.create_rectangle(x-5,y-5,x+5,y+5,fill=farba)
