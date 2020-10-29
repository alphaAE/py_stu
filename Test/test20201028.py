### 二维列表中找最大数
listP = [[12, 45, 13], [5, 67, 34], [66, 54, 15], [51, 27, 46]]

# 为maxNum赋予初值为二维列表中的第一个数值
maxNum = listP[0][0]

# 索引方式遍历列表listP
for i in range(len(listP)):
    # 使用内置函数max获取二级列表listP[i]中的最大值，并与maxNum判断大小
    if max(listP[i]) > maxNum:
        # 若当前二级列表中最大值比maxNum大，则记录下该值与该列表索引
        maxNum = max(listP[i])
        index = i

# 遍历完成后输出最大值与索引
print("最大值：{}\n所在列表二级列表索引：{}\n列表：{}".format(maxNum, index, listP[index]))


### 随机列表字典计数
import random

listNum = list()
dictNum = dict()

# 构造随机列表
for i in range(1000):
    listNum.append(random.randint(0, 100))

# 使用集合去重
dictNumOnce = set(listNum)

# 使用去重后的集合统计数量并构造字典
for i in dictNumOnce:
    dictNum[i] = listNum.count(i)

# 为字典按值降序排序
listFromDictNum = sorted(dictNum.items(), key = lambda kv: kv[1], reverse = True)

# 输出排序列表前五项
for i in range(5):
    tmpKv = listFromDictNum[i]
    print("Num:{:3}  Count:{:3}".format(tmpKv[0], tmpKv[1]))


