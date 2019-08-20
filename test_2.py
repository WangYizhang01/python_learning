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


# # pandas learning
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
#
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
# print(s3.axes)
# print(s3.dtype)
# print(s3.empty)
# print(s3[3])
# s4 = pd.Series([1,3,'cat',7,9])
# print(s4)
#
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
#
# # Panel
# data1 = np.random.rand(2,4,5)
# p = pd.Panel(data1)
# # print(data1)
# print(p)
# data2 = {'Item1' : pd.DataFrame(np.random.randn(4, 3)),
#         'Item2' : pd.DataFrame(np.random.randn(4, 2))}
# p = pd.Panel(data2)
# print(p['Item1'])


# import pandas as pd
# import numpy as np
#
# data = {'one':pd.Series(['alice','ycgd','jcus''ikhj']),'two':pd.Series([13,35,25,36,87])}
# print(data)
# s = pd.DataFrame(data,index=range(5))
# print(s)
# # print(s.T)
# print(s.axes)
# print(s.dtypes)
# print(s.empty)
# print(s.ndim)
# print(s.shape)
# print(s.size)
# print(s.values)
# print(s.head)
# print(s.tail())


# import pandas as pd
# import numpy as np
#
# d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Minsu','Jack',
#      'Lee','David','Gasper','Betina','Andres']),
#      'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
#      'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])}
#
# df = pd.DataFrame(d)
# print(df)
# print(df.sum())
# # print(sum(df))
# print(df.sum(axis=1))
# # print(df.sum(1))
# print(df.cumsum())
# print(df.mean())
# print(df.mean(axis=1))
# print(df.describe())
# print(df.describe(include=['object']))
# df.plot()


# print(type(1/2))
# class Person:
#     def __init__(self):
#         pass
#     def getAge(self):
#         print(__name__)
# p = Person()
# p.getAge()

# print(3>2>2)
# print('abc'>'xyz')

# x = input('pls enter your name: ')
# print("Hello," + x + ",how are you")
# x = 2
# print(x**2,x**3)
# a,b = map(eval,input("please enter a,b,split by space: ").split(' '))
# if a > b:
#     print("Good")
# elif a < b:
#     print("Bad")
# else:
#     print("Equal")


# #HollandRadarDraw
# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib
#
# matplotlib.rcParams['font.family']='SimHei'
# radar_labels = np.array(['研究型(I)','艺术型(A)','社会型(S)','企业型(E)','常规型(C)','现实型(R)']) #雷达标签
# nAttr = 6
# data = np.array([[0.40, 0.32, 0.35, 0.30, 0.30, 0.88],
#                  [0.85, 0.35, 0.30, 0.40, 0.40, 0.30],
#                  [0.43, 0.89, 0.30, 0.28, 0.22, 0.30],
#                  [0.30, 0.25, 0.48, 0.85, 0.45, 0.40],
#                  [0.20, 0.38, 0.87, 0.45, 0.32, 0.28],
#                  [0.34, 0.31, 0.38, 0.40, 0.92, 0.28]]) #数据值
# data_labels = ('艺术家', '实验员', '工程师', '推销员', '社会工作者','记事员')
# angles = np.linspace(0, 2*np.pi, nAttr, endpoint=False)
# data = np.concatenate((data, [data[0]]))
# angles = np.concatenate((angles, [angles[0]]))
# fig = plt.figure(facecolor="white")
# plt.subplot(111, polar=True)
# plt.plot(angles,data,'o-', linewidth=1, alpha=0.2)
# plt.fill(angles,data, alpha=0.25)
# plt.thetagrids(angles*180/np.pi, radar_labels,frac=1.2)
# plt.figtext(0.52, 0.95, '霍兰德人格分析', ha='center', size=20)
# legend = plt.legend(data_labels, loc=(0.94, 0.80), labelspacing=0.1)
# plt.setp(legend.get_texts(), fontsize='large')
# plt.grid(True)
# plt.savefig('holland_radar.jpg')
# plt.show()


# a = {1,4,7,4,7}
# print(len(a))

# print(type(1))
# print(dir(1))

# c = [1,2]
# a,b = c
# print(a,b)


# class Student:
#     def __init__(self):
#         self.sname = ''
#         self.mscore = 0
#         self.cscore = 0
#         self.escore = 0
#
#     def sum(self):
#         return self.mscore + self.cscore + self.escore
#
#
# student1 = Student()
# student2 = Student()
#
# student1.sname,student2.sname = input("name: ").split()
# student1.mscore,student2.mscore = map(eval,input("mscore: ").split())
# student1.cscore,student2.cscore = map(eval,input("cscore: ").split())
# student1.escore,student2.escore = map(eval,input("escore: ").split())
#
# if student1.sum() > student2.sum():
#     print(student1.sname,student1.mscore,student1.cscore,student1.escore)
# else:
#     print(student2.sname, student2.mscore, student2.cscore, student2.escore)


# lis = list(map(eval,input("a list of number, split by space: ").split()))
# sum = eval(input("enter the sum；"))
#
# for i in range(len(lis)-1):
#     for j in range(i+1,len(lis)):
#         if lis[i] + lis[j] == sum:
#             res = [i,j]
#             res.sort()
#             print(res)

# a = [1,2,3,4,5]
# x,y = a[:-1],a[-1]
# print(x)
# print(y)

# def tribonacci(n):
#     res = []
#     while len(res) <= n:
#         if len(res) < 2:
#             res.append(len(res))
#             continue
#         res.append(sum(res[-3:]))
#     return max(res)
#
# print(tribonacci(4))

# res = [1,2]
# print(sum(res[-6:]))

# print('110101001'.count('1'))
# print(bin(23)[2:].count('1'))

# import pprint
# print('fsatdg'[0])
# print(len('yhxay'))
# dp = [[None for _ in range(8)] for _ in range(10)]
# pprint.pprint(dp)

# import numpy as np
#
# list1 = np.array([1,2]);list2 = np.array([2,3])
# print(sum(np.square(list1,list2)))
# print('ATGhda'.lower())
#
# s = 'abcdefghijk'
# s1 = s[::-1]
# print(s,s1)


# def isPalindrome(s):
#     if not s:
#         return True
#     s = s.lower()
#     s = s.replace(' ', '')
#     for i in s:
#         if i in ",:":
#             s = s.replace(i, '')
#     s1 = s[::-1]
#     if s == s1:
#         return True
#     return False
#
# print(isPalindrome("A man, a plan, a canal: Panama"))


# a = filter(str.isalnum,'tgdy131')
# print(a)

# n = bin(6)[2:]
# m = n.split('1')
# print(n)
# print(m)
# print(n.index('1'))

# def binaryGap(N):
#     string = bin(N)[2:].split('1')[1-1]
#     max = -1
#     for i in string:
#         if len(i) > max:
#             max = len(i)
#     return max+1
#
# print(binaryGap(41))

# a = [1,2,3,4,5,6,7,8,9,0]
# b = a[:5]
# print(b)

# def binaryGap(N):
#     str1 = bin(N)[2:].split('1')
#     string = str1[1:-1]
#     max = -1
#     for i in string:
#         if len(i) > max:
#             max = len(i)
#     return max + 1
#
# print(binaryGap(41))

# a = [1,2,3,4,1,6,2]
# b = set(a)
# print(a)
# print(b)

# def hanoi(n,x,y,z):
#     if n == 1:
#         print(x,'--->',z)
#     else:
#         hanoi(n-1,x,z,y)
#         print(x,'--->',z)
#         hanoi(n-1,y,x,z)
#
# while True:
#     n = int(input("请输入汉诺塔的层数： "))
#     hanoi(n,'x','y','z')

# print(1==1==2)

# x = [1,2,3,4,1,5,6,7,8]
# print(x.index(1))
# x.remove(1)
# print(x.index(1))

# def missingNumber(nums):
#     nums.sort()
#     n = len(nums)
#
#     if nums == [0]:
#         return 1
#     elif nums == [1]:
#         return 0
#
#     for i in range(n - 1):
#         while i <= n-2:
#             if nums[i + 1] != nums[i] + 1:
#                 return nums[i] + 1
#                 break
#         else:
#             return n
#
# print(missingNumber([3,0,1]))


# def hammingWeight(n):
#     n = str(n)
#     count = 0
#     for i in n:
#         if i == '1':
#             count += 1
#     return count
#
# def hammingWeight2(n):
#     n = str(n)
#     return n.count('1')
#
# print(hammingWeight('00000000000000000000000000001011'))
# print(hammingWeight2('00000000000000000000000000001011'))


# def rob(nums):
#     n = len(nums)
#     sum1, sum2 = 0, 0
#     if n % 2 == 0:
#         for i in range(n/2):
#             sum1 += nums[2*i+1]
#             sum2 = sum(nums) - sum1
#             return sum1 if sum1 >= sum2 else
#             return sum2
#         else:
#             for i in range((n+1)/2):
#                 sum1 += nums[2i+1]
#                 sum2 = sum(nums) - sum1
#                 return sum1 if sum1 >= sum2 else
#                 return sum2


# a = [1,1,2,3,4,4,5]
# b = set(a)
#
# print(a)
# print(b)


# def hasGroupsSizeX(deck):
#     a = set(deck)
#     b = []
#     for i in a:
#         b.append(deck.count(i))
#     if len(b) == 1:
#         return True
#     for i in range(len(b) - 1):
#         for j in range(i + 1, len(b)):
#             if b[i] % b[j] != 0:
#                 return False
#     return True
#
# print(hasGroupsSizeX([1]))

# import numpy as np
#
# print(np.square(4))

# from collections import Counter
# c = 'acascse'
# a = Counter(c)
# print(a)
# print(type(a))

# digits = [1,2,3]
# digits = list(map(str,digits))
# a = ''.join(digits)
# print(a)
# print(type(a))

# nums = [1,5,3,4,7,6]
#
# num = sorted(nums)
# print(num)


# def movesToMakeZigzag(nums):
#     count1 = 0;count2 = 0;count3 = 0;count4 = 0
#     n = len(nums)
#     if n >= 2:
#         if n % 2 == 0:
#             for i in range(1, int(n / 2)):
#                 if nums[2 * i] > nums[2 * i - 1] or nums[2 * i] > nums[2 * i + 1]:
#                     nums[2 * i] -= 1
#                     count1 += 1
#                 if nums[0] > nums[1]:
#                     nums[0] -= 1
#                     count1 += 1
#             for i in range(int(n / 2) - 1):
#                 if nums[2 * i + 1] > nums[2 * i] or nums[2 * i + 1] > nums[2 * i + 2]:
#                     nums[2 * i + 1] -= 1
#                     count2 += 1
#                 if nums[n - 1] > nums[n - 2]:
#                     nums[n - 1] -= 1
#                     count2 += 1
#             return max(count1, count2)
#         else:
#             for i in range(1, int((n + 1) / 2) - 1):
#                 if nums[2 * i] > nums[2 * i - 1] or nums[2 * i] > nums[2 * i + 1]:
#                     nums[2 * i] -= 1
#                     count3 += 1
#                 if nums[0] > nums[1]:
#                     nums[0] -= 1
#                     count3 += 1
#                 if nums[n - 1] > nums[n - 2]:
#                     nums[n - 1] -= 1
#                     count3 += 1
#             for i in range(int((n + 1) / 2) - 1):
#                 if nums[2 * i + 1] > nums[2 * i] or nums[2 * i + 1] > nums[2 * i + 2]:
#                     nums[2 * i + 1] -= 1
#                     count4 += 1
#             return max(count3, count4)
#     else:
#         return 1


# dict = {'a':1,'b':2,'c':3,'d':4,'e':5}

# for i in dict.keys():
#     if i == 'b':
#         print(dict[i])
# else:
#     print(-1)
#
# print('a' in dict.keys())

# print(ord('a'))
# print(ord("A"))
# print(chr(122))

# def toLowerCase(str):
#     # return str.lower()
#     for i in str:
#         if ord(i) in list(range(65, 91)):
#             i = chr(ord(i) + 32)
#     return str
#
# print(toLowerCase('Hello'))

# data = [1,2,3,4,5,6,7,8,9,0]
#
# for i in data:
#     i = -1
# print(data)
#
# print(len('abcd'))

# def findLHS(nums):
#     from collections import Counter
#     a = Counter(nums)
#     b = sorted(a)
#     m = 0
#     for i in range(len(b) - 1):
#         j = b[i + 1]
#         k = b[i]
#         if j - k == 1:
#             m = max(m, a[j] + a[k])
#     return m

# print('abcdefg'.reverse())

# s = [0,1,2,3,4,5,6,7,8]
# print(s[1:4])
# print(s[4:1:-1])

# def dayOfYear(date):
#     date = list(map(int,date.split('-')))
#     res = 0
#     for i in range(1, date[1]):
#         if i in [1, 3, 5, 7, 8, 10, 12]:
#             res += 31
#         elif i in [4, 6, 9, 11]:
#             res += 30
#         elif date[0] % 4 == 0:
#             res += 28
#         else:
#             res += 29
#     res += date[2]
#     return res
#
# print(dayOfYear('2003-03-01'))

# print(str(100)[1])

# def relativeSortArray(arr1,arr2):
#     arr = []
#     array = []
#     for i in arr2:
#         count = arr1.count(i)
#         arr.extend([i] * count)
#     for j in arr1:
#         if j not in arr2:
#             array.append(j)
#     array.sort()
#     arr.extend(array)
#     return arr
#
# print(relativeSortArray([2,3,1,3,2,4,6,7,9,2,19],[2,1,4,3,9,6]))

# filename = 'test_r.txt'
#
# with open(filename,'r') as f:
#     cotents = f.readlines()
#
# a = ''
# for line in cotents:
#     a += (line.strip() + ' ')
#
# print(a)

# import json
#
# numbers = [1,2,3,4,5,6,7,8,9]
#
# filename = 'test_0813.json'
# with open(filename,'w') as f:
#     json.dump(numbers,f)
#
# with open(filename,'r') as f:
#     res = json.load(f)
# print(res)

# S = 'abbaca'
# S = S.replace(S[2],'')
# print(S)

# arr = [4,2,7,4,7,8,9,6,5,7]
# for i,num in enumerate(arr):
#     print(i,num)


# # 1.29
# from itertools import permutations
#
# res = []
# s = ['c','a','t','d','o','g']
# num = list(range(6))
# pailie = list(permutations(num))
# # print(len(pailie))
# # print(type(pailie[1]))
#
# for i in range(len(pailie)):
#     a = ''
#     for j in range(6):
#         a += s[pailie[i][j]]
#     res.append(a)
#
# print(res)

# def function29():
#     temp = ['c', 'a', 't', 'd', 'o', 'g']
#     from itertools import permutations
#     print(list(map(''.join, permutations(temp))))
#
# function29()

# # 1.30
# n = eval(input("Pls enter a number: "))
# if n <= 2:
#     print("The number is too small!")
# count = 0
# while n > 2:
#     n //=2
#     count += 1
# print(count)

# # 1.31
# n,m = list(map(eval,input("pls enter the number n,m: ").split(',')))
# if n > m:
#     print("The money is not enogh!")
# elif n == m:
#     print("Over!")
# else:
#     k = m - n # 假定k小于100，且货币有50,20,10,5,1
#     if k >= 50:
#         print("one 50.")
#         k -= 50
#     elif k >= 40:
#         print("two 20.")
#         k -= 40
#     elif k >= 20:
#         print("one 20.")
#         k -= 20
#     elif k >= 10:
#         print("one 10.")
#         k -= 10
#     elif k >= 5:
#         print("one 5.")
#         k -= 5
#     else:
#         print(str(k)+" 1.")

# def function31():
#     coins = {'0.5': 0, '1': 0, '5': 0, '10': 0, '20': 0, '50': 0, '100': 0}
#     temp = input("Please input Pay and Total money: \n").split(" ")
#     pay, total = int(temp[0]), int(temp[1])
#     rest = total - pay
#
#     coins[100] = int(rest / 100)
#     rest = int(rest % 100)
#     coins[50] = int(rest / 50)
#     rest = int(rest % 50)
#     coins[20] = int(rest / 20)
#     rest = int(rest % 20)
#     coins[10] = int(rest / 10)
#     rest = int(rest % 10)
#     coins[5] = int(rest / 5)
#     rest = int(rest % 5)
#     coins[1] = int(rest / 1)
#     rest = int(rest % 1)
#     coins[0.5] = int(rest / 0.5)
#     rest = int(rest % 0.5)
#
#     return coins.values()
#
# print(function31())

# # 1.32
# def function32():
#     temp = input("Please input Number1 Operation Number2: \n").split(" ")
#     num1 = int(temp[0])
#     num2 = int(temp[2])
#     oper = str(temp[1])
#     if oper == '+':
#         result = num1 + num2
#     elif oper == '-':
#         result = num1 - num2
#     elif oper == '*':
#         result = num1 * num2
#     elif oper == '/':
#         result = num1 / num2
#     else:
#         raise EOFError("Error Input!")
#     return result
#
# print(function32())

# # 1.36
# shuru = input("pls enter the words list: ").split(' ')
# shuchu = []
# for i in range(len(shuru)):
#     shuchu.append(shuru.count(shuru[i]))
# print(shuchu)


# # 冒泡排序
# def maopao(array):
#     if len(array) == 0:
#         return array
#     for i in range(len(array)):
#         for j in range(len(array)-1-i):
#             if array[j] > array[j+1]:
#                 array[j],array[j+1] = array[j+1],array[j]
#     return array
#
# def maopao2(array):
#     if len(array) < 2:
#         return array
#     for i in range(len(array)-1):
#         if array[i] > array[i+1]:
#             array[i], array[i+1] = array[i+1], array[i]
#     return maopao2(array[:-1]) + list(array[-1])
#
# array = [2,7,5,9,3,6,7,4]
# print(maopao2(array))

# # 选择排序
# b = []
#
# def xuanze(array):
#     if len(array) < 2:
#         return b
#     global b
#     min = 10
#     for i in range(len(array)):
#         if array[i] < min:
#             min = array[i]
#     array.remove(min)
#     b.append(min)
#     return xuanze(array)

# def xuanze2(array):
#     b = []
#     min = 10
#     while len(array) > 2:
#         for i in range(len(array)):
#             if array[i] < min:
#                 min = array[i]
#         del array[i]
#         b.append(min)
#     b = b + array
#     return b

# def xuanze3(array):
#     # if len(array) == 1:
#     #     return array
#     for i in range(len(array)):
#         min = i
#         for j in range(i,len(array)):
#             if array[j] < array[min]:
#                 min = j
#         array[i],array[min] = array[min],array[i]
#     return array
#
# array = [6]
# # array = [2,7,5,9,3,6,7,4]
# print(xuanze3(array))

# # 插入排序
# def charu(array):
#     if len(array) == 1:
#         return array
#     for i in range(1,len(array)):
#         for j in range(0,i):
#             if array[i-j-1] > array[i-j]:
#                 array[i-j],array[i-j-1] = array[i-j-1],array[i-j]
#     return array
#
# array = [2,7,5,9,3,6,7,4]
# print(charu(array))

# print(int('-1'))

# def reverse(x):
#     x = str(x)
#     if x[0] == '-':
#         x = x[1::-1]
#         x = '-' + x
#     else:
#         x = x[::-1]
#     return x
#
# print(reverse(-123))

# x = '-123'
# n = len(x)
# x = x[n:0:-1]
# print(x)

# print(2**31)

# print(2==2==2)

# s = ["flower","flow","flight"]
# print(min(s))
# print(max(s))
# print("flower" > "flight")

# print(list(zip(s)))
# print(list(zip(*s)))
# ss = list(map(set, zip(*s)))
# print(ss)

# N = 10
# for i in range(N, 1, -1):
#     print(i)

