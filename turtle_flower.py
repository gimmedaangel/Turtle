import turtle
t = turtle.Turtle()
t.color("red", "orange")
t.begin_fill()
t.speed(400)
for i in range(800):

    t.fd(140)
    t.rt(175)
    t.fd(140)
t.end_fill()

turtle.done()
