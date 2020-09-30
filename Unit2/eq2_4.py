import turtle as t
t.color("red", "yellow")
t.speed(10)
# t.delay(0)

t.begin_fill()
while True:
    t.forward(200)
    t.left(120)

    if abs(t.pos()) < 1:
        break
t.end_fill()

t.exitonclick()