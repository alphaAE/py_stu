import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, median_absolute_error, r2_score

#使用一元线性回归
data = np.loadtxt("DataSource/SO2.txt", delimiter=",", dtype=np.float)
X = data[:, 0].reshape((-1, 1))
y = data[:, 1].reshape((-1, 1))
# print(X)
# print(y)
# linear_model = LinearRegression()
# linear_model.fit(X,y)
# y_predict = linear_model.predict(X)
# print("MSE:",mean_squared_error(y,y_predict))

poly = PolynomialFeatures(degree=3)
x_train = poly.fit_transform(X)

linear_model = LinearRegression()
linear_model.fit(x_train, y)
y_predict = linear_model.predict(x_train)
print("MSE:", mean_squared_error(y, y_predict))
