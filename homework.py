import turtle
turtle.Screen().bgcolor("sky blue")
turtle.Screen().setup(400,600)
squre=turtle.Turtle()
sides=4
length=50
angle=360/sides
for i in range(sides):
    squre.forward(length)
    squre.left(angle)
turtle.done()




