import os
import subprocess
from productController import ProductController


# 菜单逻辑
class ConsoleUI:

    # 程序开关
    programSwitch = True

    def __init__(self):
        # 初始化菜单映射表
        self.menuList = [
            {"id": 1, "name": "显示当前超市商品清单", "fun": self.showProductList},
            {"id": 2, "name": "显示用户购物清单", "fun": self.showShoppingList},
            {"id": 3, "name": "添加商品", "fun": self.addProduct},
            {"id": 4, "name": "修改商品数量", "fun": self.modifyProduct},
            {"id": 5, "name": "删除已购商品", "fun": self.removeProduct},
            {"id": 6, "name": "退出程序", "fun": self.exitProgram},
        ]
        # 初始化商品数据控制器
        self.productController = ProductController()
        self.runMainloop()

    # 程序主循环
    def runMainloop(self):
        while self.programSwitch:
            # 打印菜单并等待输入
            execution = False
            self.showMenu()
            try:
                userInId = int(input("\n键入[功能序号]："))
            except Exception:
                self.cls()
                print("\n输入有误！")
                continue
            for item in self.menuList:
                if item["id"] == userInId:
                    execution = True
                    item["fun"]()
                    break
            # 无对应项输出
            if execution is False:
                self.cls()
                print("无对应选项")

    # 打印菜单
    def showMenu(self):
        print("\n----菜单----")
        for item in self.menuList:
            print("{}. {}".format(item["id"], item["name"]))

    # 打印当前超市商品清单
    def showProductList(self):
        self.cls()
        print("\n----商品清单----")
        # 遍历展示从商品控制器获得的商品列表
        for item in self.productController.getProduct():
            print("{}.{:<28}  单价:{}".format(
                item["id"], item["name"], item["price"]))

    # 打印用户购物清单
    def showShoppingList(self):
        self.cls()
        print("----购物清单----")
        # 遍历展示从商品控制器获得的商品列表
        index = 1
        for item in self.productController.getShopping():
            name = self.productController.getProduct(item["productId"])["name"]
            print("{}.{:<28}  数量:{}".format(index, name, item["count"]))
            index += 1

    # 添加物品
    def addProduct(self):
        # 显示菜单便于输入物品
        self.showProductList()
        try:
            productId = int(input("\n输入[添加物品序号]："))
            productCount = int(input("输入[物品数]："))
        except Exception:
            self.cls()
            print("\n输入有误！")
            return
        # 调用控制器添加方法
        returnMsg = self.productController.addProductToShoppingList(
            productId, productCount)
        self.cls()
        # 处理结果
        print("{}".format(returnMsg["msg"]))
        # 结果正常则展示购物清单
        if returnMsg["code"] == ProductController.SUCCESS:
            self.showShoppingList()

    # 修改物品数量
    def modifyProduct(self):
        # 显示购物清单便于查找物品
        self.showShoppingList()
        try:
            productIndex = int(input("\n输入[修改物品序号]："))
            productId = self.productController.getShopping(
                productIndex - 1)["productId"]
            productCount = int(input("输入[物品数]："))
        except Exception:
            self.cls()
            print("\n输入有误！")
            return
        # 调用控制器修改方法
        returnMsg = self.productController.modifyProductFromShoppingList(
            productId, productCount)
        self.cls()
        # 处理结果
        print("{}".format(returnMsg["msg"]))
        # 结果正常则展示购物清单
        if returnMsg["code"] == ProductController.SUCCESS:
            self.showShoppingList()

    # 删除商品
    def removeProduct(self):
        # 显示购物清单便于查找物品
        self.showShoppingList()
        try:
            productIndex = int(input("\n输入[修改物品序号]："))
            productId = self.productController.getShopping(
                productIndex - 1)["productId"]
        except Exception:
            self.cls()
            print("\n输入有误！")
            return
        # 调用控制器添加方法
        returnMsg = self.productController.removeProductFromShoppingList(
            productId)
        self.cls()
        # 处理结果
        print("{}".format(returnMsg["msg"]))
        # 结果正常则展示购物清单
        if returnMsg["code"] == ProductController.SUCCESS:
            self.showShoppingList()

    # 关闭程序
    def exitProgram(self):
        self.programSwitch = False

    # 清屏公用方法
    def cls(self):
        os.system("cls")
        subprocess.call("cls", shell=True)
