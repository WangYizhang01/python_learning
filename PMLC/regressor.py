import sys
import numpy as np
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt
# import cPickle as pickle

# filename = 'data_singlevar.txt'
# filename = sys.argv[1]
# x = []
# y = []
# with open(filename,'r') as f:
#     for line in f.readlines():
#         xt,yt = [float(i) for i in line.split(',')]
#         x.append(xt)
#         y.append(yt)

filename = 'data_singlevar.txt'
x = []
y = []
with open(filename,'r') as f:
    for line in f.readlines():
        xt,yt = [float(i) for i in line.split(',')]
        x.append(xt)
        y.append(yt)

num_training = int(0.8 * len(x))
num_test = len(x) - num_training

# 训练数据
x_train = np.array(x[:num_training]).reshape((num_training,1))
y_train = np.array(y[:num_training])

# 测试数据
x_test = np.array(x[num_training:]).reshape((num_test,1))
y_test = np.array(y[num_training:])

# # 创建线性回归对象
# linear_regressor = linear_model.LinearRegression()
#
# # 用训练数据集训练模型
# linear_regressor.fit(x_train,y_train)
#
# y_train_pred = linear_regressor.predict(x_train)
# plt.figure()
# plt.scatter(x_train,y_train,color='green')
# plt.plot(x_train,y_train_pred,color='black',linewidth=4)
# plt.title('Train data')
# plt.show()
#
# y_test_pred = linear_regressor.predict(x_test)
#
# plt.scatter(x_test,y_test,color='green')
# plt.plot(x_test,y_test_pred,color='black',linewidth=4)
# plt.title('Test data')
# plt.show()

# 多项式回归
polynomial = PolynomialFeatures(degree=3)

x_train_transformed = polynomial.fit_transform(x_train)
datapoint = [0.39,2.78,7.11]
poly_datapoint = polynomial.fit_transform(datapoint)

poly_linear_model = linear_model.LinearRegression()
poly_linear_model.fit(x_train_transformed,y_train)
print("\nLinear regression: ",linear_regressor.predict(datapoint)[0])
print("\nPolynomial regression:", poly_linear_model.predict(poly_datapoint)[0])