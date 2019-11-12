import tkinter
import random
X_MAX, Y_MAX = 800, 600
canvas= tkinter.Canvas(width=X_MAX, height=Y_MAX)
canvas.pack()

p= random.randint(5,10)
b=5

def stvorec(x,y,a):
    for i in range(1,p):
        canvas.create_line(x-a/2,y-a/2,x+a/2,y-a/2)
        canvas.create_line(x-a/2,y+a/2,x+a/2,y+a/2)
        canvas.create_line(x-a/2,y-a/2,x-a/2,y+a/2)
        canvas.create_line(x+a/2,y-a/2,x+a/2,y+a/2)
        a=a+b

for i in range(1,10):
    stvorec(random.randint(200,X_MAX-200),random.randint(200,Y_MAX-200),random.randint(150,300))
