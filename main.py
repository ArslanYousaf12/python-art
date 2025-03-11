# import turtle
import turtle as t
# from turtle import *
# import heroes
# print(heroes.gen())

# from turtle import Turtle, Screen, turtle
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
t.colormode(255)
def random_colors():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    rColor = (r,g,b)
    return rColor

# lineColor = ["plum", "olive", "salmon", "orange"]


# def moveRight(angel):
#     timy.forward(100)
#     timy.right(angel)
    
# def drawShape(sides):
#     for _ in range(sides):
#         penColor = random.choice(lineColor)
#         timy.pencolor(penColor)
#         moveRight(total_angel/sides)
direction = [0, 90,180, 270]

timy = t.Turtle()
timy.shape("turtle")
timy.pensize(5)
timy.speed("fast")
for _ in range(100):
    turtle_direction = random.choice(direction)
    timy.pencolor(random_colors())
    timy.forward(15)
    timy.setheading(turtle_direction)

# total_angel = 360
# for num in range(3, 11):
#     print(num)
#     drawShape(num)



        




screen = t.Screen()
screen.exitonclick()