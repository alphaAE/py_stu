import matplotlib.pyplot as plt
import numpy as np
from sklearn import tree
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, binarize
from sklearn.tree import plot_tree
import graphviz
import math


def gain(data):
    count = data.shape[0]
    weight1 = data[data['y'] == 0].shape[0] / count
    weight2 = data[data['y'] == 1].shape[0] / count

    return -weight1 * math.log(weight1, 2) - weight2 * math.log(weight2, 2)


# 使用信息熵计算二值化分界阈值（不一定能写完）
def infoGainBinarize(data, indexList):
    print(data)
    # divisionPoint = map()
    for index in indexList:
        # 去重 & 排序
        vList = list(set(data[index]))
        vList.sort()
        # 计算每两个值间的均值作为阈值候选列表
        candidateList = list()
        for i in range(vList.__len__() - 1):
            candidateList.append((vList[i] + vList[i + 1]) / 2)
        # 划分前的信息熵
        firstGain = gain(data)
        print(firstGain)
        # 遍历查找信息增益最大对应的划分点
        for candidate in candidateList:
            pass


#读数据集
def process_data():
    data = pd.read_csv("./DataSource/bank-full.csv", delimiter=";")
    #删除空值
    data = data.dropna()

    # Test 取样 人为二值化连续数据
    data = data[["age", "job", "y"]]
    # data['age'] = binarize([data['age']], threshold=44.5)[0]

    # 获取keys
    keys = data.keys()
    # keys = keys.drop(["day", "month", "pdays"])
    # 将文本数据转换为数字类别
    data = data[keys].apply(LabelEncoder().fit_transform)

    infoGainBinarize(data, ["age"])

    X = data.iloc[:, :-1]
    y = data.iloc[:, -1]
    X_train, X_test, y_train, y_test = train_test_split(X,
                                                        y,
                                                        test_size=0.33,
                                                        random_state=42)
    return X_train, X_test, y_train, y_test


#决策树算法
def desicionTree(X_train, X_test, y_train, y_test):
    model = tree.DecisionTreeClassifier()
    model.fit(X_train, y_train)
    y_predict = model.predict(X_test)
    # 渲染dot到pdf
    dot_data = tree.export_graphviz(model,
                                    feature_names=["age", "job"],
                                    filled=True,
                                    rounded=True)
    graph = graphviz.Source(dot_data)
    graph.render("tree")

    plot_tree(model, feature_names=["age", "job"])
    plt.show()

    return y_predict


#评价 score
def score(y_test, y_pred):
    print("准确率：", accuracy_score(y_test, y_pred))


if __name__ == "__main__":
    X_train, X_test, y_train, y_test = process_data()
    # y_pred = desicionTree(X_train, X_test, y_train, y_test)
    # score(y_test, y_pred)
