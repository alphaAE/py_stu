### DataFrame练习
# 生成数据
import pandas as pd
import numpy as np

df = pd.DataFrame()
index = ["alpha", "beta", "gamma", "delta", "eta"]
for i in range(5):
    a = pd.DataFrame([np.linspace(i, 5 * i, 5)], index=[index[i]])
    df = pd.concat([df, a], axis=0)

print(df, "\n")

# 获取列数据
print(df[[1, 2]], "\n")

# 修改列名
df.columns = ["a", "b", "c", "d", "e"]
print(df, "\n")

# 获取第二列数据
print(df["b"], "\n")
# print(df.b, "\n")
# print(df.iloc[:, 1], "\n")
# print(df.loc[:, "b"], "\n")

# # 取出 a,d列数据
print(df[["a", "d"]], "\n")

# # 获取 c列下的beta值
print(df["c"]["beta"], "\n")    # 显式
print(df["c"][1], "\n")         # 隐式
print(df.iloc[1, 2], "\n")
print(df.loc["beta", "c"], "\n")
