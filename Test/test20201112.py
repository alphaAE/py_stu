# 菜品选择价格计算
def selectFood():
    sum = 0
    showFoodLibrary()
    while True:
        try:
            tmpVId = int(input("采购菜品ID:"))
            tmpVNum = int(input("已选择[{}] 采购数量:".format(foodLibrary[tmpVId - 1][0])))
            sum += foodLibrary[tmpVId - 1][1] * tmpVNum

            if int(input("当前合计：{}$\n是否追加菜品？（1.是 2.否[结算并回到菜单]）:".format(sum))) == 2:
                break
        except Exception:
            print("输入有误!")
    print("合计总价：{:.2f}$".format(sum))


def showFoodLibrary():
    print("------------------------------------")
    print("菜品列表：")
    for i in range(len(foodLibrary)):
        print("{}.{} {}$".format(i + 1, foodLibrary[i][0], foodLibrary[i][1]))


def showMenuList():
    print("------------------------------------")
    print("选择功能：")
    for i in range(len(menuList)):
        print("{}.{}".format(i + 1, menuList[i][0]))
    try:
        select = int(input())
        menuList[select - 1][1]()
    except Exception:
        print("输入有误!")


menuList = [
    ["查看菜品列表", showFoodLibrary],
    ["选择菜", selectFood]
]
foodLibrary = [
    ["白菜", 2.71],
    ["豆干", 5.43],
    ["胡豆", 4.76],
    ["笋尖", 3.68]
]


def main():
    while True:
        showMenuList()


if __name__ == '__main__':
    main()
