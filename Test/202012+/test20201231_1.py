import turtle

num = 18
_len = 20


liftRot = 180 - ((num - 2) * 180 / num)
print(liftRot)

turtle.pendown()
turtle.begin_fill()
turtle.pencolor(1, 0, 1)
turtle.pensize(5)
turtle.fillcolor(0, 0, 1)

for i in range(num):
    turtle.fd(_len)
    turtle.left(liftRot)
    turtle.fd(_len)
    turtle.right(liftRot * 2)

turtle.end_fill()
turtle.penup()
turtle.done()
