import turtle

#六边形
turtle.pendown()
for i in range(6):
    turtle.fd(50)
    turtle.left(180 - ((6 - 2) * 180 / 6))
turtle.penup()


turtle.setpos(-100, -100)

#六角星
turtle.pendown()
for i in range(6):
    turtle.fd(50)
    turtle.left(180 - ((6 - 2) * 180 / 6))
    turtle.fd(50)
    turtle.right(360 - 2 * (180 - (180 - ((6 - 2) * 180 / 6))))
turtle.penup()

turtle.done()
