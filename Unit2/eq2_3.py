import turtle as t
import random

t.setup(650, 350, 200, 200)
t.speed(10)
# t.delay(0)

t.penup()
t.fd(-250)
t.pendown()
t.pensize(25)
t.pencolor("purple")
t.seth(-40)
for i in range(4):
    t.pencolor(random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1))
    t.circle(40, 80)
    t.circle(-40, 80)

# 尾部
t.pencolor(random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1))
t.circle(40, 80 / 2)
t.fd(40)
t.circle(16, 180)
t.fd(40 * 2 / 3)


t.exitonclick()