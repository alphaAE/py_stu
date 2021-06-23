迷茫中被开了这门机器学习课程，记得导师'周昊'开课时说着这课不是给我们这个阶段的学生学习的，原想着会教的相对轻松些，没想到还是对我的高数知识弱区一顿打击。转眼就要结课考试，故在这里对整个学期的教学内容进行简单归纳，项目的仓库(github)地址放在最后，方便对照查看。

# 流程

## 数据预处理

读入数据并进行一定调整、分割

注意：

* 数据去重
* 处理异常值(含空值)
* 字符串类型的映射处理
* 数值离散化
* 划分训练集与测试集

## 建立模型

编写算法或使用sklearn库中特定封装方法进行训练与预测

## 预测/评价

对模型的预测进行评价

> 回归评价指标

| name         | function                               |
| :----------- | :------------------------------------- |
| 平均绝对误差 | mean_absolute_error(y, y_predict)      |
| 均方误差     | mean_squared_error(y, y_predict)       |
| 中值绝对误差 | median_absolute_error(y, y_predict)    |
| 可解释方差值 | explained_variance_score(y, y_predict) |
| R方值        | r2_score(y, y_predict)                 |

> 分类评价指标

| name           | function                                                                     |
| :------------- | :--------------------------------------------------------------------------- |
| 准确性评价指标 | accuracy_score(y, y_predict)                                                 |
| 精确率评价指标 | precision_score(y, y_predict)                                                |
| 召回率评价指标 | recall_score(y, y_predict)                                                   |
| ROC曲线        | fpr, tpr, thresholds = roc_curve(y, y_predict) </br> plt.plot(fpr, tpr, ...) |

# 算法归类

## 回归

> 多元线性回归模型

对连续值进行预测

Code:
T0324_multivariate_linear_regression_sklearn

> 批量梯度下降

批量梯度下降：在梯度下降的每一步中都用到了所有的训练样本。
思想：找能使代价函数减小最大的下降方向（梯度方向）。
损失函数（loss function）：通常用损失函数来度量拟合的程度。损失函数极小化，意味着拟合程度最好，对应的模型参数即为最优参数。

Code:
T0407_batch_gradient_descent
T0414_mini_batch_gradient_descent
T0414_stochastic_batch_gradient_descent

> 多项式回归

多项式回归是多元线性回归的一个特例，使用曲线来拟合数据

Code:
T0414_polynomial_regression


## 分类

> Logistic回归

Logistic回归是机器学习中最常用最经典的分类方法之一，使用拟合直线进行二分类和多分类

Code:
T0421_logistic_regression(二分类)
T0519_Iris_multi_category(多分类)

> 决策树

决策树是一种树型结构，其中每个内部节结点表示在一个属性上的测试，每一个分支代表一个测试输出，每个叶结点代表一种类别。

在决策树的算法中，建立决策树的关键，即在当前状态下选择哪个属性作为分类依据。根据不同的目标函数，建立决策树主要有一下三种算法：

* ID3
* C4.5
* CART

主要的区别就是选择的目标函数不同，ID3使用的是信息增益，C4.5使用信息增益率，CART使用的是Gini系数。

Code:
T0602_decisionTree_entropy

> 支持向量机（Support Vector Machine, SVM）

支持向量机（Support Vector Machine, SVM）是一类按监督学习（supervised learning）方式对数据进行二元分类的广义线性分类器（generalized linear classifier），其决策边界是对学习样本求解的最大边距超平面（maximum-margin hyperplane）

Code:
T0609_SVM

> 朴素贝叶斯分类

朴素贝叶斯方法是在贝叶斯算法的基础上进行了相应的简化，即假定给定目标值时属性之间相互条件独立。也就是说没有哪个属性变量对于决策结果来说占有着较大的比重，也没有哪个属性变量对于决策结果占有着较小的比重。

Code:
T0616_naive_bayes

# 相关内容

* 仓库地址

(若github访问不稳定请自备梯子)