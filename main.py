from turtle import Turtle
import turtle as t
import random
radiusOfCircle =100
point=t.Turtle()
t.colormode(255)
colors=["CornflowerBlue","red","lime","deep sky blue","magenta","blue violet"]
def genarate_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    return(r,g,b)

directions=[0,90,180,270]
point.shape("turtle")
point.pensize(10)
point.speed("fastest")
# for i in range(200):
#     point.color(genarate_color())
#     point.forward(20)
#     point.right(random.choice(directions))
def change_heading():
    point.setheading(point.heading()+10)
def setRadious():
    global radiusOfCircle
    radiusOfCircle +=10
for j in range(100,200,10):
    for i in range(0,200):
        point.circle(radiusOfCircle)
        change_heading()
    radiusOfCircle +=10
    point.color(genarate_color())

screen = t.Screen()
screen.exitonclick()