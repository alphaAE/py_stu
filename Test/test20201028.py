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
