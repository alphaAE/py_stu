### 生日悖论
import random


def sam():
    brithday = []
    res = []
    for i in range(1000):
        n = random.randint(1, 365)
        brithday.append(n)

    for j in range(23):
        k = brithday[random.randint(0, 999)]
        res.append(k)

    for i in range(1, 23):
        for j in range(i):
            if res[i] == res[j]:
                return True
    return False


counts = 0
for i in range(100):
    if sam():
        counts += 1
    else:
        continue
print("至少两人相同的概率是{}%".format(counts))
