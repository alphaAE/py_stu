###
# web = ["星期天", "星期一", "星期二", "星期三", "星期四", "星期五", "星期六"]
# while True:
#     day = int(input("输入天数："))
#     print("该天为：{}".format(web[day % 7]))

###
# text = "school"
# bText = ""
# cText = ""
# for i in text:
#     bText += chr(ord(i) + 8)
# print(bText)
# for j in bText:
#     cText += chr(ord(j) - 8)
# print(cText)

import time
# t = time.clock()

### \r 动态刷新条
for i in range(101):
    print("\r [{}{}] {}%".format(">" * i, "-" * (100 - i), i), end="")
    time.sleep(0.02)
print()

import math
### 两位数的公约数
numArr = [12, 40]
gcd = math.gcd(numArr[0], numArr[1])
for i in range(numArr[0], 0, -1):
    if numArr[0] % i == 0 and numArr[1] % i == 0:
        gcd = i
        break
print("最大公约数：{}".format(gcd))
