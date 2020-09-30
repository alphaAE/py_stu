import turtle as t

def PrintTri(pos, len, startAngle):
    t.setpos(pos[0], pos[1])
    t.pendown()
    for i in range(3):
        t.seth(i * 120 + startAngle)
        t.fd(len)
    t.penup()


PrintTri([0, 0], 100, 0)
PrintTri([50, -33], 100, 60)

t.done()
