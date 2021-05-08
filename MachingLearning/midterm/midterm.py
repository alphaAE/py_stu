# 数据集说明：该数据集是为了从印度的角度预测研究生入学率而创建的。
# 数据集Feature包括：
# 1。编号
# 2。GRE成绩（满分340分）
# 3。托福成绩（满分120分）
# 4。大学评分（满分5分）
# 5。目的陈述和推荐信强度（满分5分）
# 6。本科GPA（满分10分）
# 7。研究经历（0或1）
# Label：研究生录取概率（从0到1）

# 要求：
# 1、用自己熟悉的方法独立编程实现这个对数几率回归问题。
# 2、模型训练好了需要可视化。
# 3、要输出训练好的模型的参数。
# 4、请用熟知的评价方法对你训练好的模型进行评价。
# 5、遇到代码上的问题可以百度搜索，严禁交头接耳互相讨论。
# 6、如有发现雷同代码，直接计0分。
# 7、请直接将写好的代码复制粘贴至这里，作出的图片也直接上传这里即可，无需另外上传文件。

import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import SGDRegressor
from sklearn import linear_model
from sklearn.metrics import mean_absolute_error, mean_squared_error, median_absolute_error, explained_variance_score, r2_score


#数据预处理
def process_data():
    data = np.loadtxt("./MachingLearning/midterm/Admission_Predict.csv",
                      delimiter=",",
                      skiprows=1,
                      dtype=np.float)

    X = data[:, 1:-1]
    y = data[:, -1]
    X_train, X_test, y_train, y_test = train_test_split(X,
                                                        y,
                                                        test_size=0.33,
                                                        random_state=42)

    #标准化
    scaler = StandardScaler()
    # 计算均值和方差
    scaler.fit(X_train)
    # 将数据集标准化
    X_train = scaler.transform(X_train)
    X_test = scaler.transform(X_test)

    return X_train, X_test, y_train, y_test


# 训练模型
def fit_model(X_train, y_train):
    # 梯度下降法优化
    model = SGDRegressor()
    model.fit(X_train, y_train)
    # 广义线性（弃用）
    # model = linear_model.LinearRegression()
    # model.fit(X_train, y_train)
    # 截距
    print("模型截距：{}".format(model.intercept_))
    # 权重
    print("模型权重：{}".format(model.coef_))
    return model


# 预测 & 评价
def score(y_test, y_predict):
    # 评价
    print("平均绝对误差：{}".format(mean_absolute_error(y_test, y_predict)))
    print("均方误差：{}".format(mean_squared_error(y_test, y_predict)))
    print("中值绝对误差：{}".format(median_absolute_error(y_test, y_predict)))
    print("可解释方差值：{}".format(explained_variance_score(y_test, y_predict)))
    print("R方值：{}".format(r2_score(y_test, y_predict)))

    # 模型可视化（散点）
    #真实值
    plt.scatter(range(len(y_test)), y_test, c="g", alpha=0.5)
    #预测值
    plt.scatter(range(len(y_test)), y_predict, c='r', alpha=0.5)
    plt.show()

    # 模型可视化（线性）
    # plt.plot(range(len(y_test)), y_test, c="red", alpha=0.5)
    # plt.plot(range(len(y_test)), y_predict, c="blue", alpha=0.5)
    # plt.show()


if __name__ == "__main__":
    X_train, X_test, y_train, y_test = process_data()
    model = fit_model(X_train, y_train)
    y_predict = model.predict(X_test)
    score(y_test, y_predict)
