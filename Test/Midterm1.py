# 1 Turtle绘制
import turtle as t
t.color("red", "yellow")
t.speed(10)

t.left(36)

t.begin_fill()
while True:
    t.forward(100)
    t.left(180 - 36)

    if abs(t.pos()) < 1:
        break
t.end_fill()

t.penup()
t.seth(0)
t.goto(100 + 40, 0)
t.pendown()
t.write("李昕辰")

# 隐藏画笔
t.hideturtle()
t.exitonclick()
