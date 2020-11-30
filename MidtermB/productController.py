# 数据控制器
class ProductController:

    # 商品列表数据模板
    productList = [
        {"id": 1, "name": "疯狂Python讲义", "price": 88.0},
        {"id": 2, "name": "疯狂Java讲义", "price": 69.0},
        {"id": 3, "name": "疯狂Android讲义", "price": 59.0},
        {"id": 4, "name": "Python爬虫实战讲义", "price": 109.0},
        {"id": 5, "name": "Python数据分析与可视化讲义", "price": 108.0},
        {"id": 6, "name": "Python计算机视觉讲义", "price": 77.0}
    ]

    # 购物清单数据模板
    shoppingList = [
        {"productId": 1, "count": 10},
        {"productId": 3, "count": 5},
        {"productId": 4, "count": 1}
    ]

    # 成功常量
    SUCCESS = 0
    # 返回消息示集
    returnMsg = {
        0: {"code": 0, "msg": "成功"},
        1: {"code": 1, "msg": "列表中已存在该商品"},
        2: {"code": 2, "msg": "修改的商品不存在"},
        3: {"code": 3, "msg": "删除的商品不存在"},
        4: {"code": 4, "msg": "添加的商品不存在"}
    }

    def __init__(self):
        # 构造时清空购物清单
        self.shoppingList.clear()

    # 获取商品列表
    def getProduct(self, id=-1):
        if id < 0:
            return self.productList
        else:
            for item in self.productList:
                if id == item["id"]:
                    return item
            return False

    # 获取购物清单
    def getShopping(self, index=-1):
        if index < 0:
            return self.shoppingList
        else:
            return self.shoppingList[index]

    # 添加商品
    def addProductToShoppingList(self, productId, count):
        # 商品存在检查
        exist = False
        for item in self.productList:
            if item["id"] == productId:
                exist = True
        if exist is False:
            return self.returnMsg[4]
        # 重复添加检查
        for item in self.shoppingList:
            if item["productId"] == productId:
                return self.returnMsg[1]
        # 通过检查则添加至列表并返回成功消息
        self.shoppingList.append({"productId": productId, "count": count})
        return self.returnMsg[0]

    # 修改商品数量
    def modifyProductFromShoppingList(self, productId, count):
        # 商品存在检查
        for i in range(0, len(self.shoppingList)):
            item = self.shoppingList[i]
            if item["productId"] == productId:
                # 查询到则修改数值并返回成功
                self.shoppingList[i]["count"] = count
                return self.returnMsg[0]
        # 不存在则返回错误
        return self.returnMsg[2]

    # 删除商品
    def removeProductFromShoppingList(self, productId):
        # 商品存在检查
        for i in range(0, len(self.shoppingList)):
            item = self.shoppingList[i]
            if item["productId"] == productId:
                # 查询到则抛出该商品并返回成功
                self.shoppingList.pop(i)
                return self.returnMsg[0]
        # 不存在则返回错误
        return self.returnMsg[3]
