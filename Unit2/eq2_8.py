import turtle as t

t.speed(0)

t.pendown()
for len in range(0, 300, 3):
    t.left(90)
    t.fd(len)
t.penup()

t.done()
