# # 面向对象
# class Dog:
#     """一个模拟狗的类"""
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def bark(self):
#         print(self.name + " can bark.")
#
# dog = Dog('ZHA',12)
# # dog.bark()
# def info(self):
#     print(self.name,self.age)
#
# dog.inf = info
# dog.inf(dog)
# dog.inf()


# # 数列的层次图
# class Progression:
#     """一个数列基类"""
#     def __init__(self,start=0):
#         self._current = start
#
#     def _advance(self):
#         self._current += 1
#
#     def __next__(self):
#         if self._current is None:
#             raise StopIteration()
#         else:
#             answer = self._current
#             self._advance()
#             return answer
#
#     def __iter__(self):
#         return  self
#
#     def print_progression(self):
#         print(' '.join(str(next(self)) for j in range(n)))
#
#
# class ArthmeticProgression(Progression):
#     """一个表示等差数列的类"""
#     def __init__(self,increment=1,start=0):
#         super().__init__(start)
#         self._increment = increment
#
#     def _advance(self):
#         self._current += self._increment
#
#
# class GeometicProgression(Progression):
#     """一个表示等比数列的类"""
#     def __init__(self,base=2,start=0):
#         super().__init__(start)
#         self._base = base
#
#     def _advance(self):
#         self._current *= self._base
#
#
# class FibonacciProgression(Progression):
#     """一个表示斐波那契数列的类"""
#     def __init__(self,first=0,second=1):
#         super().__init__(first)
#         self._prev = second - first
#
#     def _advance(self):
#         self._prev,self._current = self._current,self._prev + self._current


