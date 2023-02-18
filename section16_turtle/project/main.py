import colorgram
# วาดรูป 10 เเถวเเถวละ 10 จุด 

rgb_colors = []
colors = colorgram.extract('section16_turtle/project/image.jpg', 30)       #         
for color in colors:
    rgb_colors.append(color.rgb)

print(rgb_colors)