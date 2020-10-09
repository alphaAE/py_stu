import turtle as t
import random

t.setup(650, 350, 200, 200)
t.speed(0)
t.delay(0)

t.pencolor("purple")
t.pensize(25)
t.pendown()

for i in range(0, 1600, 1):
    t.pencolor(random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1))
    t.circle(i, 12)

t.exitonclick()