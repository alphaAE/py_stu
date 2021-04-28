import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_score, recall_score, accuracy_score, roc_curve


#数据预处理
def process_data():
    data = np.loadtxt("./DataSource/pima-indians-diabetes.data.csv",
                      delimiter=",",
                      skiprows=1,
                      dtype=np.float)
    X = data[:, :-1]
    y = data[:, -1]
    mu = X.mean(0)
    std = X.std(0)
    X = (X - mu) / std
    X_train, X_test, y_train, y_test = train_test_split(X,
                                                        y,
                                                        test_size=0.33,
                                                        random_state=42)
    return X_train, X_test, y_train, y_test


#评价指标函数
def score(y_test, y_predict):
    print("准确性评价指标:", accuracy_score(y_test, y_predict))
    print("精确率评价指标:", precision_score(y_test, y_predict))
    print("召回率评价指标:", recall_score(y_test, y_predict))
    fpr, tpr, thresholds = roc_curve(y_test, y_predict)
    plt.rcParams["font.sans-serif"] = ["SimHei"]
    plt.title("ROC曲线")
    plt.xlabel("假正率FPR")
    plt.ylabel("真正率TPR")
    plt.plot(fpr, tpr, linewidth=2, linestyle='-', color="red")
    plt.show()


if __name__ == "__main__":
    X_train, X_test, y_train, y_test = process_data()
    logist = LogisticRegression()
    logist.fit(X_train, y_train)
    y_predict = logist.predict(X_test)
    score(y_test, y_predict)
    # print(y_predict[:10])
    # print(y_test[:10])
