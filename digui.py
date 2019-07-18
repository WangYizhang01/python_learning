# # 递归
# def fact(n):
#     if n == 0:
#         return 1
#     return n*fact(n-1)
#
# print(fact(5))
#
# # 字符串反转
# # s = 'abcdefghijk'
# # print(s[::-1])
# def rvs(s):
#     if s == '':
#         return s
#     else:
#         return rvs(s[1:]) + s[0]
#
# # 斐波那契数列
# def fib(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
#
# # 汉诺塔问题
# count = 0
#
# def hanoi(n,src,dst,mid):
#     global count
#     if n == 1:
#         print("{}:{}->{}".format(1,src,dst))
#         count += 1
#     else:
#         hanoi(n-1,src,mid,dst)
#         print("{}:{}->{}".format(n,src, dst))
#         count += 1
#         hanoi(n-1,mid,dst,src)
#
# hanoi(10,"A","C","B")
# print(count)
#
# # 科赫曲线
# #KochDrawV1.py
# import turtle
# def koch(size, n):
#     if n == 0:
#         turtle.fd(size)
#     else:
#         for angle in [0, 60, -120, 60]:
#            turtle.left(angle)
#            koch(size/3, n-1)
# def main():
#     turtle.setup(800,400)
#     turtle.penup()
#     turtle.goto(-300, -50)
#     turtle.pendown()
#     turtle.pensize(2)
#     koch(600,3)     # 0阶科赫曲线长度，阶数
#     turtle.hideturtle()
# main()
#
# #KochDrawV2.py
# import turtle
# def koch(size, n):
#     if n == 0:
#         turtle.fd(size)
#     else:
#         for angle in [0, 60, -120, 60]:
#            turtle.left(angle)
#            koch(size/3, n-1)
# def main():
#     turtle.setup(600,600)
#     turtle.penup()
#     turtle.goto(-200, 100)
#     turtle.pendown()
#     turtle.pensize(2)
#     level = 3      # 3阶科赫雪花，阶数
#     koch(400,level)
#     turtle.right(120)
#     koch(400,level)
#     turtle.right(120)
#     koch(400,level)
#     turtle.hideturtle()
# main()