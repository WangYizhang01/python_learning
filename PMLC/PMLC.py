import numpy as np
import scipy
from sklearn import preprocessing
import matplotlib

# # 数据预处理
# data = np.array([[3,-1.5,2,-5.4],[0,4,-0.3,2.1],[1,3.3,-1.9,-4.3]])
#
# data_standardized = preprocessing.scale(data)# 标准化
# print("\nMean = ",data_standardized.mean(axis=0))
# print("Std deviation = ",data_standardized.std(axis=0))
#
# data_scaler = preprocessing.MinMaxScaler(feature_range=(0,1))# 范围缩放
# data_scaled = data_scaler.fit_transform(data)
# print("\nMin max scaled data = ",data_scaled)
#
# data_normalized = preprocessing.normalize(data,norm='l1')# 归一化
# print("\nL1 normalized data = ",data_normalized)
#
# data_binarized = preprocessing.Binarizer(threshold=1.4).transform(data)# 二值化
# print("\nBinarized data = ",data_binarized)

# # 标记编码
# label_encoder = preprocessing.LabelEncoder()# 创建一个标记编码器
#
# input_classes = ['audi','ford','audi','toyota','ford','bmw']
# label_encoder.fit(input_classes)
# print("\nClass mapping:")
# for i,item in enumerate(label_encoder.classes_):
#     print(item , "-->" , i)

