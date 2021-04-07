import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error, mean_squared_error, median_absolute_error, explained_variance_score, r2_score


# 特征归一化
def featureNormalize(X):
    # 列均值
    mu = X.mean(0)
    sigma = np.std(X)
    X = (X - mu) / sigma
    index = np.ones((len(X), 1))
    X = np.hstack((X, index))
    return X


# 数据预处理
def getDataFrom():
    data = np.loadtxt("./DataSource/aqi2.csv",
                      delimiter=",",
                      skiprows=1,
                      dtype=float)
    X = data[:, 1:]
    y = data[:, 0]
    # 改变 lable 集的形状
    y = y.reshape(-1, 1)
    # 归一化处理
    X = featureNormalize(X)
    return X, y


# 损失函数
def lossFunction(X, y, theta):
    m = len(X)
    L = sum((np.dot(X, theta) - y)**2) / (2 * m)
    return float(L)


# 梯度下降算法
def gradiebtDecent(X, y, theta, alpha, num_iters):
    lossList = list()
    m = len(X)
    for i in range(num_iters):
        theta = theta - alpha * np.dot(X.T, (np.dot(X, theta)) - y) / m
        L = lossFunction(X, y, theta)
        lossList.append(L)
    return theta, lossList


if __name__ == "__main__":
    X, y = getDataFrom()
    theta = np.ones([X.shape[1], 1])
    alpha = 0.01
    num_iters = 2000
    # 计算梯度下降
    theta, lossList = gradiebtDecent(X, y, theta, alpha, num_iters)
    # print(lossList, end="\n\n")

    # 预测结果计算
    y_predict = np.dot(X, theta)

    # 评价结果
    print("平均绝对误差：{}".format(mean_absolute_error(y, y_predict)))
    print("均方误差：{}".format(mean_squared_error(y, y_predict)))
    print("中值绝对误差：{}".format(median_absolute_error(y, y_predict)))
    print("可解释方差值：{}".format(explained_variance_score(y, y_predict)))
    print("R方值：{}".format(r2_score(y, y_predict)))
