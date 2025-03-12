import colorgram

colors = colorgram.extract('image.jpg',10)
color_list = []
for num in range(10):
    selected_color = colors[num]
    rgb = selected_color.rgb
    red = rgb.r
    green = rgb.g
    blue = rgb.b
    rgb_color = (red, green, blue)
    color_list.append(rgb_color)
print(color_list)
print(colors)
# print(colors)
print(len(colors))