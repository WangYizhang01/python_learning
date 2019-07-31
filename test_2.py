# import random
#
# u = random.randint(0,9)
# print(u)

# u = 3
# if u == 3:
#     raise ValueError('wrong')
# else:
#     print(u)

# a = [1,2,4,'gse','ux']
# b = '|'.join(map(str,a))
# print(b)

# import numpy as np
# import random
#
# a = np.arange(9).reshape(3,3)
# print(a[1])
# print(a[:,1])
# print(a[1][1])
# board = np.array([[' '] * 9 for j in range(9)])
# for i in range(50):
#     while True:
#         u = random.randint(0,8)
#         v = random.randint(0,8)
#         k = random.randint(0,9)
#         if board[u][v] != ' ':
#             continue
#         elif k in board[u] or k in board[:,v]:
#             continue
#         else:
#             board[u][v] = k
#             break
#
# for i in range(9):
#     print('  |  '.join(map(str,board[i])))
#
# list1 = [1,2,3]
# list1 = np.array(list1)
# list2 = np.ones(3)
# print(list1 + list2)
# print(list1.max())
# print(list1.min())
# print(max(list1))
#
# mat1 = np.array([[1,2,3,4],[5,6,7,8]])
# mat2 = np.ones((2,4))
# print(mat1.max(axis=1))
# print(mat1)
# print(mat1.T)
# error = 1/4 * np.sum(np.square(mat1[0] - mat2[0]))
# print(error)

# print(list('ABCD'))

# pandas learning
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# # Series
# s = pd.Series([1,3,5,np.nan,6,8])
# print(s)
#
# df2 = pd.DataFrame({ 'A' : 1.,
#                      'B' : pd.Timestamp('20170102'),
#                      'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
#                      'D' : np.array([3] * 4,dtype='int32'),
#                      'E' : pd.Categorical(["test","train","test","train"]),
#                      'F' : 'foo' })
#
# print(df2)
# print(df2.head())
# print(df2.tail(1))
# print(df2.info())
# print(df2.index)
# s1 = pd.Series(5,index=list(range(4)))
# print(s1)
# s2 = pd.Series([1,3,5,7,9])
# print(s2)
# print(s2[0])
# print(s2[:3])
# print(s2[-3:])
# s3 = pd.Series(list(range(5)),index=list(range(2,7)))
# print(s3)
# print(s3[3])
# s4 = pd.Series([1,3,'cat',7,9])
# print(s4)

# # Dataframe
# df1 = pd.DataFrame()
# print(df1)
# df2 = pd.DataFrame([1,2,3,4,5,6])
# print(df2)
# data1 = [['Alex',13],['Bob',9],['Clare',19]]
# df3 = pd.DataFrame(data1,index=range(1,4),columns=['name','age'])
# print(df3)
# dict1 = {'name':['Alex','Bob','Clare','Dod'],'age':[14,42,26,35]}
# df4 = pd.DataFrame(dict1,index=['rank1','rank2','rank3','rank4'])
# print(df4)
# data2 = [{'a':1,'b':2,'c':3},{'b':6,'c':7,'d':8}]
# df5 = pd.DataFrame(data2,index=['fir','sec'])
# print(df5)
# dict2 = {'one': pd.Series([1, 2, 3],index=['a', 'b', 'c']),
#          'two': pd.Series([1, 2, 3, 4],index=['a', 'b', 'c', 'd'])}
#
# df6 = pd.DataFrame(dict2)
# print(df6)
# # 列操作
# print(df6['one'])
# df6['three'] = pd.Series([10,20,30],index=['a','b','c'])
# df6['four'] = df6['one'] + df6['three']
# print(df6)
# del df6['one']
# print(df6)
# df6.pop('two')
# print(df6)
# # 行操作
# print(df6.loc['b'])
# print(df6.iloc[2])
# print(df6[2:4])
# df7 = pd.DataFrame([[1, 2], [3, 4]], columns = ['a','b'])
# df8 = pd.DataFrame([[5, 6], [7, 8]], columns = ['a','b'])
# df9 = df7.append(df8)
# print(df9)
# df9 = df9.drop(0)
# print(df9)

# Panel
