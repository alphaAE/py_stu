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

for i in range(100):
    print("\r [{}{}] {}%".format(">" * i, "-" * (100 - i), i), end="")
    time.sleep(0.1)

### 两位数的公约数
