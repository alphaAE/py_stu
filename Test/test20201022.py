### 
import random
numList = list(range(100))

luckNum = random.choice(numList)
random.shuffle(numList)

for i in numList:
    if i == luckNum:
        print("恭喜，号码[{}]中奖了！".format(i))
        break
    else:
        print("抱歉，号码[{}]没有中奖。".format(i))

### 冒泡
numList = list(range(100))
random.shuffle(numList)


### 进度条 20 后低速 到 30 - 100 加速

