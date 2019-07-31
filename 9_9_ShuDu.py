# 9*9数独游戏
import random
import numpy as np
# random.seed(7)

class ShuDu:
    def __init__(self, n):
        """初始化棋盘"""
        self._board = np.array([[' '] * 9 for j in range(9)])
        for i in range(n):
            while True:
                u = random.randint(0,8)
                v = random.randint(0,8)
                k = random.randint(0,9)
                if self._board[u][v] != ' ':
                    continue
                elif k in self._board[u] or k in self._board[:,v]:
                    continue
                else:
                    self._board[u][v] = k
                    break

    def mark(self, i, j, k):
        if not (0 <= i <= 8 and 0 <= j <= 8):
            raise ValueError('Invalid board position')
        if self._board[i][j] != ' ':
            raise ValueError('Board position occupied')
        if k in self._board[i][:] or k in self._board[:][j]:
            raise ValueError('This key is existed.')
        self._board[i][j] = k

    def is_win(self):
        for i in range(9):
            for j in range(9):
                if self._board[i][j] == ' ':
                    return True
                # else:
                #     print("game is continuing.")

    def Print(self):
        for i in range(9):
            print('  |  '.join(map(str,self._board[i])))


shudu = ShuDu(40)
shudu.Print()
# while shudu.is_win():
#     i,j,k = map(int,input("Please enter the i,j,k: ").split())
#     # i = int(i);j = int(j);k =int(k)
#     shudu.mark(i,j,k)
#     shudu.Print()