import matplotlib.pyplot as plt
import numpy as np
from sklearn import tree
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB, MultinomialNB
from sklearn.preprocessing import LabelEncoder, Binarizer
from sklearn.tree import plot_tree
import graphviz


#读数据集
def process_data():
    data = pd.read_csv("./DataSource/bank-full.csv", delimiter=";")
    #删除空值
    data = data.dropna()
    print(data)

    # Test
    data = data[["age", "job", "y"]]
    # 二值化连续数据
    bn = Binarizer(threshold=44.5)
    ageBn = bn.fit_transform([data['age']])[0]
    data['age'] = ageBn
    print(data)

    # 获取keys
    keys = data.keys()
    # keys = keys.drop(["day", "month", "pdays"])
    # 将文本数据转换为数字类别
    data = data[keys].apply(LabelEncoder().fit_transform)

    print(data)
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

    return y_predict


#评价 score
def score(y_test, y_pred):
    print("准确率：", accuracy_score(y_test, y_pred))


if __name__ == "__main__":
    X_train, X_test, y_train, y_test = process_data()
    y_pred = desicionTree(X_train, X_test, y_train, y_test)
    score(y_test, y_pred)
