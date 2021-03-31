import numpy as np
from numpy.linalg import inv
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import linear_model
import pickle

# 数据预处理
data = np.loadtxt("./DataSource/aqi2.csv",
                  delimiter=",",
                  skiprows=1,
                  dtype=float)

# data = np.hstack((data, np.ones((data.shape[0], 1))))
X = data[:, 1:]
y = data[:, 0]

# 划分数据集为训练集与测试集
X_train, X_test, y_train, y_test = train_test_split(X,
                                                    y,
                                                    test_size=0.33,
                                                    random_state=42)

model = linear_model.LinearRegression()
model.fit(X_train, y_train)
# 权重
print(model.coef_)
# 截距
print(model.intercept_)

y_predict = model.predict(X_test)

# 模型可视化
plt.plot(range(len(X_test)), y_test, c="red", alpha=0.5)
plt.plot(range(len(X_test)), y_predict, c="blue", alpha=0.5)
plt.show()

with open("./MachingLearning/model.pickle", "wb") as f:
    pickle.dump(model, f)
