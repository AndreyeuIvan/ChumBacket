import turtle
import colorsys

def draw_one_color_arc(x,y,r,pensize,color):
    turtle.up();turtle.goto(x+r,y)
    turtle.down();turtle.seth(90)
    turtle.pensize(pensize);turtle.pencolor(color)
    turtle.circle(r,180)

turtle.speed(0)
turtle.hideturtle()
turtle.bgcolor('light blue')
turtle.title('49-Color Raindow')
turtle.setup(700, 700)
num_color = 49

radius = 300
penwidth = 20*7/num_color
hue = 0
for i in range(num_color):
    (r,g,b) = colorsys.hsv_to_rgb(hue, 1, 1)
    draw_one_color_arc(0, -100, radius, penwidth, (r,g,b))
    radius -= (penwidth-1)
    hue += 0.9/num_color
turtle.getscreen()._root.mainloop()
