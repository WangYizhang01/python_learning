# """利用适配器模式基于数组实现栈"""
# class ArrayStack:
#     """LIFO Stack implementation using a Python list as underlying storage"""
#
#     def __init__(self):
#         """Create an empty stack."""
#         self._data = []
#
#     def __len__(self):
#         return len(self._data)
#
#     def is_empty(self):
#         # if len(self._data) == 0:
#         #     return True
#         # return False
#         return len(self._data) == 0
#
#     def push(self,e):
#         self._data.append(e)
#
#     def top(self):
#         if self.is_empty():
#             raise Empty('Stack is empty')
#         return self._data[-1]
#
#     def pop(self):
#         if self.is_empty():
#             raise Empty('Stack is empty')
#         return self._data.pop()
#
#
# stack = ArrayStack()
# for i in range(1,11):
#     stack.push(i)
#
# # print(stack.top())
# # print(stack.pop())
# # print(stack.top())
#
# # 逆置一个栈
# stack_2 = ArrayStack()
# for i in range(10):
#     stack_2.push(stack.pop())
#
# # print(stack_2.top())
#
# # 逆置一个文件的各行
# def reverse_file(filename):
#     """逆置一个文件的各行"""
#     S = ArrayStack()
#     original = open(filename)
#     for line in original:
#         S.push(line.rstrip('\n'))
#     original.close()
#
#     output = open(filename,'w')
#     while not S.is_empty():
#         output.write(S.pop() + '\n')
#     output.close()
#
# # reverse_file('test.txt')
#
# # 分隔符匹配算法
# def is_matched(expr):
#     lefty = '({['
#     righty = ')}]'
#     S = ArrayStack()
#     for c in expr:
#         if c in lefty:
#             S.push(c)
#         elif c in righty:
#             if S.is_empty():
#                 return False
#             if righty.index(c) != lefty.index(S.pop()):
#                 return False
#     return S.is_empty()
#
# print(is_matched('[(5+x)-(y+z)]'))


"""利用适配器模式基于数组实现队列"""
class ArrayQueue:
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._front]

    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer

    def enqueue(self,e):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def _resize(self,cap):
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0