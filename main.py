# import turtle
# import turtle as t
# from turtle import *
# import heroes
# print(heroes.gen())

from turtle import Turtle, Screen
import random

# def move_right():
#     timy_the_turtle.right(90)
#     timy_the_turtle.forward(100)

# timy_the_turtle = Turtle()
# timy_the_turtle.shape("turtle")
# timy_the_turtle.color("red")
# timy_the_turtle.forward(100)
# for _ in range(3):
#     move_right()
# def movePenDown():
#     timy.pendown()
#     timy.forward(10)

# def movePenUp():
#     timy.penup()
#     timy.forward(10)
lineColor = ["plum", "olive", "salmon", "orange"]


def moveRight(angel):
    timy.forward(100)
    timy.right(angel)
    
def drawShape(sides):
    for _ in range(sides):
        penColor = random.choice(lineColor)
        timy.pencolor(penColor)
        moveRight(total_angel/sides)


timy = Turtle()
timy.shape("turtle")
total_angel = 360
for num in range(3, 11):
    print(num)
    drawShape(num)



        




screen = Screen()
screen.exitonclick()