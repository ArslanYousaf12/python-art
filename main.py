# import turtle
# import turtle as t
# from turtle import *
# import heroes
# print(heroes.gen())

from turtle import Turtle, Screen

def move_right():
    timy_the_turtle.right(90)
    timy_the_turtle.forward(100)

timy_the_turtle = Turtle()
timy_the_turtle.shape("turtle")
timy_the_turtle.color("red")
timy_the_turtle.forward(100)
for _ in range(3):
    move_right()
    




screen = Screen()
screen.exitonclick()