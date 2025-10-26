import turtle
turtle.Screen().bgcolor("light pink")
turtle.Screen().setup(400,600)
pentagon=turtle.Turtle()
sides=5
length=50
angle=360/sides
for i in range(sides):
    pentagon.forward(length)
    pentagon.left(angle)
turtle.done()




