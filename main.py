# import colorgram

# colors = colorgram.extract('image.jpg',10)
# color_list = []
# for num in range(10):
#     selected_color = colors[num]
#     rgb = selected_color.rgb
#     red = rgb.r
#     green = rgb.g
#     blue = rgb.b
#     rgb_color = (red, green, blue)
#     color_list.append(rgb_color)
# print(color_list)
# print(colors)
# # print(colors)
# print(len(colors))
# from turtle import Turtle, Screen
import turtle as t
import random
t.colormode(255)
colors_list = [ (234, 225, 83), (195, 8, 69), (231, 54, 132), (194, 164, 15), (112, 178, 214), (199, 77, 15)]

timy = t.Turtle()
timy.pensize(5)
timy.penup()
timy.hideturtle()
timy.setpos(-255.00,-255.00)
for _ in range(10):
    for _ in range(25):
        timy.pencolor(random.choice(colors_list))
        # timy.fillcolor(random.choice(colors_list))
    
        timy.dot()
        timy.forward(20)
    timy.backward(20 * 25)
    timy.left(90)
    timy.forward(20)
    timy.right(90)

   






my_screen = t.Screen()
my_screen.exitonclick()