# # 第一章
# # 二分查找
# def binary_search(list,item):
#     low = 0
#     high = len(list) - 1
#
#     while low <= high:
#         mid = int((low + high)/2)
#         guess = list[mid]
#         if guess > item:
#             high = mid - 1
#         elif guess < item:
#             low = mid + 1
#         else:
#             return mid
#     return None
#
# my_list = [1,3,5,7,0,9]
#
# print(binary_search(my_list,0))


# # 第二章
# # 选择排序
# # 查找给定数组的最小值的索引
# def search_min(arr):
#     min = 0
#     for i in range(len(arr)):
#         if arr[i] < arr[min]:
#             min = i
#     return min
#
# # 对数组进行排序
# def sort_list(arr):
#     new_arr = []
#     for i in range(len(arr)):
#         new_arr.append(arr[search_min(arr)])
#         del arr[search_min(arr)]
#     return new_arr
#
# list_0 = [58,21,72,9,24,16,58,43,66,84,24]
# print(sort_list(list_0))


# # 第三章
# # 递归
# def count(n):
#     print(n)
#     if n <= 0:
#         return
#     count(n-1)
#
# count(10)

# def count(n):
#     print(n)
#     while n >= 0:
#         count(n-1)
#
# count(2)

# # 递归实现列表求和
# def sum(list_1):
#     if len(list_1) == 0:
#         return 0
#     # if len(list_1) == 1:
#     #     return list_1[0]
#     return list_1[0] + sum(list_1[1:])
#
# l = [1,2,3,4,5,6,7,8,9]
# print(sum(l))

# 递归实现快速排序
def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([10,5,2,3]))