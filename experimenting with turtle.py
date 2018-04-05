import turtle

win = turtle.Screen()
win.bgcolor("green")
t = turtle.Turtle()
t.shape("turtle")
t.color("blue")
t.speed(10)

t.penup()
size=20
for u in range(30):
    t.stamp()
    size=size+3
    t.forward(size)
    t.right(24)
    t.pendown()
