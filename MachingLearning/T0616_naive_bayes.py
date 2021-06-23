import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB, MultinomialNB
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, precision_score, recall_score


#读数据集
def process_data():
    data = pd.read_csv("e:/data/bank-full.csv", delimiter=";")
    #删除空值
    data = data.dropna()
    #获取keys
    keys = data.keys()
    keys = keys.drop(["day", "month", "pdays"])
    #将文本数据转换为数字类别
    data = data[keys].apply(LabelEncoder().fit_transform)
    # print(data)
    X = data.iloc[:, :-1]
    y = data.iloc[:, -1]
    X_train, X_test, y_train, y_test = train_test_split(X,
                                                        y,
                                                        test_size=0.33,
                                                        random_state=42)
    return X_train, X_test, y_train, y_test


#高斯贝叶斯模型
def GauNB(X_train, X_test, y_train, y_test):
    bayes = GaussianNB()
    bayes.fit(X_train, y_train)
    y_pred = bayes.predict(X_test)
    return y_pred


#多项式贝叶斯模型
def MulNB(X_train, X_test, y_train, y_test):
    bayes = MultinomialNB()
    bayes.fit(X_train, y_train)
    y_pred = bayes.predict(X_test)
    return y_pred


#评价 score
def score(y_test, y_pred):
    print("准确率：", accuracy_score(y_test, y_pred))


if __name__ == "__main__":
    X_train, X_test, y_train, y_test = process_data()
    # y_pred =  GauNB(X_train, X_test, y_train, y_test)
    y_pred = MulNB(X_train, X_test, y_train, y_test)
    score(y_test, y_pred)
