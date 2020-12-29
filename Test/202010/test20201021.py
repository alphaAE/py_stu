### 菜品选择价格计算
vArr = [
    ["白菜", 2.71],
    ["豆干", 5.43],
    ["胡豆", 4.76],
    ["笋尖", 3.68]
]
print("菜品列表：")
for i in range(len(vArr)):
    print("{}.{} {}$".format(i+1, vArr[i][0], vArr[i][1]))
print()

sum = 0.0

while True:
    try:
        tmpVId = int(input("采购菜品ID:"))
        tmpVNum = int(input("已选择[{}] 采购数量:".format(vArr[tmpVId - 1][0])))
        sum += vArr[tmpVId - 1][1] * tmpVNum
    
        if int(input("当前合计：{}$\n是否追加菜品？（1.是 2.否）:".format(sum))) == 2:
            break
    except:
        print("输入异常！")

print("合计总价：{:.2f}$".format(sum))

### 随机数游戏
import random
a = random.randint(1, 20)
count = 6
print("游戏开始！")
while True:
    if count == 0:
        print("游戏结束，你失败了，数值为 {}".format(a))
        break
    tmpNum = int(input("你还有 {}次机会 请输入：".format(count)))
    if tmpNum == a:
        print("恭喜猜中！")
        break
    else:
        print("没猜中！")
        count -= 1
        

