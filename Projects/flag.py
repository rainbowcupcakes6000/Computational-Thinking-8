import turtle
t = turtle.Turtle()

# setup
t.speed(50)
turtle.Screen().bgcolor("light blue")

h = 50
# stripes

# move to stripe 1
t.goto(-250, -170)

t.color("red")
t.begin_fill()
t.forward(500)
t.left(90)
t.forward(120)
t.left(90)
t.forward(500)
t.left(90)
t.forward(120)
t.end_fill()

t.penup()
t.goto(-250, -50)
t.pendown()

t.right(270)
t.color("green")
t.begin_fill()
t.forward(500)
t.left(90)
t.forward(120)
t.left(90)
t.forward(500)
t.left(90)
t.forward(120)
t.end_fill()

t.penup()
t.goto(-250, 70)
t.pendown()

t.right(270)
t.color("yellow")
t.begin_fill()
t.forward(500)
t.left(90)
t.forward(120)
t.left(90)
t.forward(500)
t.left(90)
t.forward(120)
t.end_fill()

turtle.exitonclick()