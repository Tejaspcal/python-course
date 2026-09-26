import turtle
turtle.Screen().bgcolor("red")
turtle.Screen().setup(300,400)
polish = turtle.Turtle()

num_sides = 7
side_length = 70
angle = 360 / num_sides

for i in range(num_sides):
    polish.forward(side_length)
    polish.right(angle)

turtle.done()