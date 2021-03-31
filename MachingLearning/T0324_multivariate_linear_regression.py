import numpy as np
from numpy.linalg import inv
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# 数据预处理
data = np.loadtxt("./DataSource/aqi2.csv",
                  delimiter=",",
                  skiprows=1,
                  dtype=float)

data = np.hstack((data, np.ones((data.shape[0], 1))))
X = data[:, 1:]
y = data[:, 0]

# 划分数据集为训练集与测试集
X_train, X_test, y_train, y_test = train_test_split(X,
                                                    y,
                                                    test_size=0.33,
                                                    random_state=42)

theta = np.dot(np.dot(inv(np.dot(X_train.T, X_train)), X_train.T), y_train)

predict = np.dot(X_test, theta)

# 模型可视化
plt.plot(range(len(X_test)), y_test, c="red", alpha=0.5)
plt.plot(range(len(X_test)), predict, c="blue", alpha=0.5)
plt.show()
