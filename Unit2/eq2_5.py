import turtle as t

nimiTriangle = False

t.color("red", "yellow")
t.speed(10)

t.begin_fill()
while True:
    t.forward(200)
    t.left(120)

    if abs(t.pos()) < 1:
        t.left(60)
        t.forward(100)
        t.right(60)
        endPos = t.pos()
        while True:
            t.forward(100)
            t.right(120)
            print("{} : {}".format(t.pos(), endPos))
            tmpPosNumX = t.pos()[0] - endPos[0]
            tmpPosNumY = t.pos()[1] - endPos[1]

            if (tmpPosNumX < 1 and tmpPosNumX > -1) and (tmpPosNumY < 1 and tmpPosNumY > -1):
                nimiTriangle = True
                break
    if nimiTriangle:
        break
        
        
t.end_fill()

t.exitonclick()