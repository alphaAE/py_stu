import random
import time

### 1
# numList = list(range(100))

# luckNum = random.choice(numList)
# random.shuffle(numList)

# for i in numList:
#     if i == luckNum:
#         print("恭喜，号码[{}]中奖了！".format(i))
#         break
#     else:
#         print("抱歉，号码[{}]没有中奖。".format(i))

### 冒泡
numList = list(range(20))
random.shuffle(numList)
print(numList)

for i in range(len(numList) - 1):
    for j in range(0, len(numList) - 1 - i):
        if numList[j] > numList[j + 1]:
            tmp = numList[j]
            numList[j] = numList[j + 1]
            numList[j + 1] = tmp

print(numList)

### 进度条 20 后低速 之后加速
sleepTime = 1.0
for i in range(101):
    if i % 20 == 0:
        sleepTime = random.choice(range(0, int(sleepTime * 100.0))) / 100.0
    print("\r [{}{}]  {}% sleepTime:{}".format(">" * i, "-" * (100 - i), i, sleepTime), end="")
    time.sleep(sleepTime)
print()
