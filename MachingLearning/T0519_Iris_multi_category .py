import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


#预处理数据
def process_data(path):
    data = pd.read_csv(path)
    # print(data)
    class_dict = {"Iris-setosa": 0, "Iris-versicolor": 1, "Iris-virginica": 2}
    data["species"] = data["species"].map(class_dict)
    # print(data)
    X = data.iloc[:, 0:-1]
    y = data.iloc[:, -1]
    X = np.array(X, dtype=np.float)
    y = np.array(y, dtype=np.float)
    mu = X.mean(0)
    std = X.std(0)
    X = (X - mu) / std
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)
    return X_train, X_test, y_train, y_test


#分类
def classifier_OVR(X_train, X_test, y_train, y_test):
    #默认是ovr的方式  一对其余
    log = LogisticRegression()
    log.fit(X_train, y_train)
    y_predict = log.predict(X_test)
    #简单评价  算预测正确率
    print("OVR正确率:", np.sum(y_predict == y_test) / len(y_test))


def classifier_OVO(X_train, X_test, y_train, y_test):
    #包含了ovo的方式  一对一
    log = LogisticRegression(multi_class="multinomial", solver="sag")
    log.fit(X_train, y_train)
    y_predict = log.predict(X_test)
    #简单评价  算预测正确率
    print("OVO正确率:", np.sum(y_predict == y_test) / len(y_test))


#主函数
if __name__ == "__main__":
    X_train, X_test, y_train, y_test = process_data("./DataSource/iris.txt")
    classifier_OVR(X_train, X_test, y_train, y_test)
    classifier_OVO(X_train, X_test, y_train, y_test)