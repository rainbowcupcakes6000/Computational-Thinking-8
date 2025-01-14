#start
import turtle

#settings
t = turtle.Turtle()
t.speed(1000000000)
turtle.Screen().bgcolor("black")
colors = ["cyan","blue","purple","white"]

#loop
for i in range(120):
    #directions and turns
    t.color( colors[i%4])
    t.forward(1 + i)
    t.left(90 + 1)

for i in range(120):
    #directions and turns
    t.color( colors[i%4])
    t.forward(1 + i)
    t.left(90 + 1)

for i in range(120):
    #directions and turns
    t.color( colors[i%4])
    t.forward(1 + i)
    t.left(90 + 1)

#keeps it up until it leaves screen
t.penup() 
for i in range(999999999):
    #directions and turns
    t.color( colors[i%4])
    t.forward(1 + i)
    t.left(90 + 1)

#End
turtle.exitonclick