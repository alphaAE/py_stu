from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import precision_score, recall_score
from sklearn.svm import SVC


#读数据
def process_data():
    data = pd.read_csv("E:/data/breast-cancer-wisconsin.csv")
    #去重
    data = data.drop_duplicates()
    #处理异常值(替换？）将？设置为Nan
    data = data[data != "?"]
    data = data.fillna(method="pad", axis=0)
    data = data.astype(int)

    X = data.iloc[:, 1:-1]
    y = data.iloc[:, -1]
    y[y == 2] = -1
    y[y == 4] = 1
    X_train, X_test, y_train, y_test = train_test_split(X,
                                                        y,
                                                        test_size=0.33,
                                                        random_state=42)
    return X_train, X_test, y_train, y_test


#建立SVM模型
def svm_model(X_train, X_test, y_train, y_test):
    svc = SVC(C=0.1)
    svc.fit(X_train, y_train)
    y_pred = svc.predict(X_test)
    return y_pred


def score(y_test, y_pred):
    print("精确率评价指标：", precision_score(y_test, y_pred))
    print("召回率评价指标：", recall_score(y_test, y_pred))


if __name__ == "__main__":
    X_train, X_test, y_train, y_test = process_data()
    y_pred = svm_model(X_train, X_test, y_train, y_test)
    score(y_test, y_pred)
