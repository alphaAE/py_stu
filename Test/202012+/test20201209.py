### DataFrame练习
import pandas
import numpy


index = ("Java", "Python", "MySQL", "Linux")
numpy.random.seed(0)
dic1 = {
    "张三": numpy.random.randint(120, 150, 4),
    "李四": numpy.random.randint(120, 150, 4),
    "王五": numpy.random.randint(120, 150, 4),
    "赵六": numpy.random.randint(120, 150, 4)
}
df1 = pandas.DataFrame(dic1, index)
numpy.random.seed(1)
dic2 = {
    "张三": numpy.random.randint(120, 150, 4),
    "李四": numpy.random.randint(120, 150, 4),
    "王五": numpy.random.randint(120, 150, 4),
    "赵六": numpy.random.randint(120, 150, 4)
}
df2 = pandas.DataFrame(dic2, index)

# 期中与期末的成绩和
print(df1 + df2, "\n")

# 期中与期末的平均值
print((df1 + df2) * 0.5, "\n")

# 张三期中Python记0
df1.at["Python", "张三"] = 0
print(df1, "\n")

# 李四期中所有加10
df1.loc[:, "李四"] += 10
print(df1, "\n")

# 所有Python成绩加15
df1.loc["Python", :] += 15
print(df1, "\n")
