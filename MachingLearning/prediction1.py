import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import tree
from sklearn.metrics import precision_score, recall_score, roc_curve
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import Binarizer
from sklearn.tree import plot_tree


#数据预处理
def preprocess(path):
    data = pd.read_csv(path)
    
    data = data.drop_duplicates()
    data = data[data != "?"]
    data = data.fillna(method="pad", axis=1)
    data = data.astype(int)

    # 删除指定列号的数据
    # data = data.drop(data.columns[[0, 1]], axis=1)
    
    X = data.iloc[:, 1:-1]
    y = data.iloc[:, -1]
    y[y == 2] = 0
    y[y == 4] = 1
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)
    return X_train, X_test, y_train, y_test


#决策树算法
def desicionTree(X_train, X_test, y_train, y_test):
    model = tree.DecisionTreeClassifier(criterion="entropy")
    model.fit(X_train, y_train)
    plot_tree(model)
    plt.show()
    y_predict = model.predict(X_test)
    return y_predict


#评价指标
def score(y_predict, y_test):
    print("正确率: ", np.sum(y_predict == y_test) / len(y_test))
    print("精确率评价指标: ", precision_score(y_test, y_predict))
    print("召回率评价指标: ", recall_score(y_test, y_predict))
    fpr, tpr, thresholds = roc_curve(y_test, y_predict)
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.plot(fpr, tpr, c="red")
    # plt.show()


#可视化
def show_plot(y_predict, y_test):
    plt.rcParams["font.sans-serif"] = ['SimHei']
    plt.title("绘制真实值与预测值")
    plt.xlabel("数量编号")
    plt.ylabel("类别")
    # 预测值
    plt.plot(range(len(y_predict)), y_predict, c='blue')
    # 真实值
    plt.plot(range(len(y_test)), y_test, c='green')
    plt.legend(["预测值", "真实值"])
    # plt.show()


if __name__ == "__main__":
    X_train, X_test, y_train, y_test = preprocess(
        "./DataSource/breast-cancer-wisconsin.csv")
    y_predict = desicionTree(X_train, X_test, y_train, y_test)
    score(y_predict, y_test)
