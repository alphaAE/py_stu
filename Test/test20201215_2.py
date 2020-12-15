import random

brandSuit = ["黑桃", "红桃", "方块", "梅花"]
brandNum = ["3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A", "2"]
brandMap = {}

# generate brandMap
for suit in brandSuit:
    tempNum = 0
    for num in brandNum:
        brandMap[(suit + num)] = tempNum
        tempNum += 1
brandMap["小王"] = 13
brandMap["大王"] = 14

# 获取所有牌面列表
brandList = list(brandMap)

# 洗牌
random.shuffle(brandList)

BrandListA = list()
BrandListB = list()
BrandListC = list()

# 发牌
while len(brandList) > 0:
    BrandListA.append(brandList.pop(0))
    BrandListB.append(brandList.pop(0))
    BrandListC.append(brandList.pop(0))

print("A的牌:" + str(BrandListA))
print("B的牌:" + str(BrandListB))
print("C的牌:" + str(BrandListC))

# 每列随机抽出一张
BrandA = random.choice(BrandListA)
BrandB = random.choice(BrandListB)
BrandC = random.choice(BrandListC)

# 比较大小
result = [(BrandA, 'A'), (BrandB, 'B'), (BrandC, 'C')]
result.sort(reverse=True, key=lambda x: brandMap[x[0]])
print("比较结果:" + str(result))

# 输出赢家结果
print("赢家为：{}".format(result[0][1]))
