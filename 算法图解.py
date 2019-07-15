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

# # 递归实现快速排序
# def quicksort(array):
#     if len(array) < 2:
#         return array
#     else:
#         pivot = array[0]
#         less = [i for i in array[1:] if i <= pivot]
#         greater = [i for i in array[1:] if i > pivot]
#         return quicksort(less) + [pivot] + quicksort(greater)
#
# print(quicksort([10,5,2,3]))

# 散列表在Python中可用字典实现
# from collections import deque
#
# graph = {}
#
# graph['you'] = ['alice','bob']
# graph['bob'] = ['anuj','peggy']
# graph['alice'] = ['peggy']
# graph['claire'] = ['thom','jonny']
# graph['anuj'] = []
# graph['peggy'] = []
# graph['thom'] = []
# graph['jonny'] = []
#
# graph['you'].append('claire')
#
# search_queue = deque()
# search_queue += graph['you']
#
# def person_is_seller(name):
#     return name[-1] == 'm'
#
# def search_mango(search_queue):
#     while search_queue:
#         person = search_queue.popleft()
#         if person_is_seller(person):
#             print(person + " is a mango seller!")
#             return True
#         else:
#             search_queue += graph[person]
#     else:
#         print("There is no mango seller!")
#         return False
#
# print(search_mango(search_queue))
#
# # 书中原代码
# def search(name):
#     search_queue = deque()
#     search_queue += graph[name]
#     searched = []
#     while search_queue:
#         person = search_queue.popleft()
#         if person not in searched:
#             if person_is_seller(person):
#                 print person + " is a mango seller!"
#                 return True
#             else:
#                 search_queue += graph[person]
#                 searched.append(person)
#     return False


# 狄克斯特拉算法实现(未理解)
graph ={}

graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {}

# 创建开销表
infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

# 创建一个存储父节点的散列表
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

processed = []

def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)

# 贪婪算法
states_needed = set(["mt","wa","or","id","nv","ut","ca","az"])

stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])
final_stations = set()

while states_needed:
    best_station = None
    states_covered = set()
    for station, states_for_station in stations.items():
        covered = states_needed & states_for_station  # 集合的交集
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered
            states_needed -= states_covered
            final_stations.add(best_station)

print(final_stations)