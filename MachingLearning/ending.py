'''
       _       _              _    _____
  __ _| |_ __ | |__   __ _   / \  | ____|
 / _` | | '_ \| '_ \ / _` | / _ \ |  _|
| (_| | | |_) | | | | (_| |/ ___ \| |___
 \__,_|_| .__/|_| |_|\__,_/_/   \_\_____|
        |_|
'''
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, binarize
import math
from sklearn.svm import SVC
from sklearn.impute import SimpleImputer
from sklearn.naive_bayes import GaussianNB, MultinomialNB
from sklearn.metrics import precision_score, recall_score, accuracy_score, roc_curve


# 数据预处理
def process_data():
    data = pd.read_csv("./DataSource/weatherAUS.csv", delimiter=",")
    # 数据太多了，我的平板跑不动，节选部分数据
    data = data.sample(n=10000, random_state=0)
    ## 数据缺失值处理
    # 异常值置为 Nan
    data = data[data != "NA"]

    # 查看缺失值的缺失情况
    print(data.isnull().mean())
    # 提取每一列的数据类型
    print(data.dtypes)

    #1 离散型变量处理
    # 找出分类型特征
    cate = data.columns[data.dtypes == "object"].tolist()
    # 除了"object"特，还有虽然用数字，但是本质为分类型特征的
    cloud = ["Cloud9am", "Cloud3pm"]
    cate = cate + cloud
    print(cate)
    # 对于分类型特征，使用众数来进行填补
    si = SimpleImputer(missing_values=np.nan, strategy="most_frequent")
    si.fit(data.loc[:, cate])
    # 使用众数来填补数据
    data.loc[:, cate] = si.transform(data.loc[:, cate])
    # 查看分类型特征是否依然存在缺失值
    print(data.loc[:, cate].isnull().mean())

    #2 连续性变量处理
    col = data.columns.tolist()
    for i in cate:
        col.remove(i)
    print(col)
    # 填补策略为"mean"
    impmean = SimpleImputer(missing_values=np.nan, strategy="mean")
    impmean = impmean.fit(data.loc[:, col])
    # 填补数据
    data.loc[:, col] = impmean.transform(data.loc[:, col])

    ## 文本数据 转换 为数字类别

    # 获取keys
    keys = data.columns[data.dtypes == "object"].tolist()
    keys.remove("Date")
    print(keys)
    # 将文本数据转换为数字类别
    tempData = data[keys].apply(LabelEncoder().fit_transform)
    # 组装回源数据
    for d in tempData.columns.tolist():
        data[d] = tempData[d]

    # 删除不必要的变量（日期）
    data = data.drop(columns=['Date'])
    print(data)

    X = tempData.iloc[:, :-1]
    y = tempData.iloc[:, -1]
    X_train, X_test, y_train, y_test = train_test_split(X,
                                                        y,
                                                        test_size=0.33,
                                                        random_state=42)
    return X_train, X_test, y_train, y_test


#高斯贝叶斯模型
def GauNB(X_train, X_test, y_train, y_test):
    bayes = GaussianNB()
    bayes.fit(X_train, y_train)
    # 输出模型参数
    print("class_count_：{}".format(bayes.class_count_))
    print("class_prior_：{}".format(bayes.class_prior_))
    print("classes_：{}".format(bayes.classes_))
    print("epsilon_：{}".format(bayes.epsilon_))
    print("sigma_：{}".format(bayes.sigma_))
    print("theta_：{}".format(bayes.theta_))
    y_pred = bayes.predict(X_test)
    return y_pred


# 评价
def score(y_test, y_pred):
    print("准确性评价指标:", accuracy_score(y_test, y_pred))
    print("精确率评价指标:", precision_score(y_test, y_pred))
    print("召回率评价指标:", recall_score(y_test, y_pred))
    fpr, tpr, thresholds = roc_curve(y_test, y_pred)
    plt.rcParams["font.sans-serif"] = ["SimHei"]
    plt.title("ROC曲线")
    plt.xlabel("假正率FPR")
    plt.ylabel("真正率TPR")
    plt.plot(fpr, tpr, linewidth=2, linestyle='-', color="red")
    plt.show()


if __name__ == "__main__":
    X_train, X_test, y_train, y_test = process_data()
    y_pred = GauNB(X_train, X_test, y_train, y_test)
    score(y_test, y_pred)
