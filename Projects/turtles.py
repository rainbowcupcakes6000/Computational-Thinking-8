import turtle

t = turtle.Turtle()
t.penup()
t.goto(-100, -100)
t.color ("cyan")
t.pendown ()

for i in range (5) :
    t.forward(100)
    t.left(72)

turtle.exitonclick()