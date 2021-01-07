# 猜数
import numpy
border = [0, 100]
num = numpy.random.randint(border[0], border[1])
bout = 0

while True:
    try:
        i = int(input("请输入值："))
        if i == num:
            print("猜中了! 数值是 {},总共猜了 {} 次".format(num, bout))
            break
        if i > num:
            border[1] = i
        else:
            border[0] = i
        bout += 1
        print("范围变更：{}".format(border))
    except Exception:
        print("Err: 输入错误！")
