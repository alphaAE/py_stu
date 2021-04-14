import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error, mean_squared_error, median_absolute_error, explained_variance_score, r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import SGDRegressor

data = np.loadtxt("./DataSource/aqi2.csv",
                  delimiter=",",
                  skiprows=1,
                  dtype=float)
X = data[:, 1:]
y = data[:, 0]

X_train, X_test, y_train, y_test = train_test_split(X,
                                                    y,
                                                    test_size=0.33,
                                                    random_state=42)

#sklearn 标准化函数
scaler = StandardScaler()
# 计算均值和方差
scaler.fix(X_train)
# 将数据集标准化
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

# 训练模型
sgd = SGDRegressor()
sgd.fit(X_train, y_train)
y_predict = sgd.predict(X_train)

# 评价结果
print("平均绝对误差：{}".format(mean_absolute_error(y, y_predict)))
print("均方误差：{}".format(mean_squared_error(y, y_predict)))
print("中值绝对误差：{}".format(median_absolute_error(y, y_predict)))
print("可解释方差值：{}".format(explained_variance_score(y, y_predict)))
print("R方值：{}".format(r2_score(y, y_predict)))

# plt.scatter()