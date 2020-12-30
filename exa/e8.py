# 5-6 科赫曲线的绘制
import turtle


def koch(size, n):
    if n == 0:
        turtle.fd(size)
    else:
        for angle in [0, 60, -120, 60]:
            turtle.left(angle)
            koch(size / 3, n - 1)


def main():
    turtle.setup(1200, 800)
    turtle.speed(0)  # 控制绘制速度
    turtle.delay(0)
    turtle.penup()
    turtle.goto(-300, -50)
    turtle.hideturtle()

    turtle.pendown()
    turtle.pensize(2)
    koch(1000, 6)     # 0阶科赫曲线长度，阶数
    turtle.done()


main()
