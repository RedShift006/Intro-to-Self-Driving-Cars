# coding:utf-8
# Implementing a Matrix Class
# In this project you will implement a Matrix class in Python. 
# Specifically, you will implement the following methods:
class Matrix(object):
    # need init function
    # Constructor

    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])



    # Primary matrix math methods
    #############################
    # determinant 是什么意思不太明白
    # 矩阵行列式 不太明白？？？？
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        det = 0
        # Check if is square
        # 检验其是否是方形矩阵
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(ValueError, "Calculating determinant not implement for matrices largerer than 2x2")

        # TODO - your code here

        # 这里仅实现了获取1x1 2x2 矩阵的det值
        # For Matrix 1x1
        if (self.h * self.w) == 1:
            det = self.grid[0][0]
        # For Matrix 2x2
        elif self.h == 2 & self.w == 2:
            det = self.g[1][1] * self.g[0][0] - self.g[0][1] * self.g[1][0]
        # In the future could implement determinant for matrix bigger
        else:
            raise(NotImplementedError, "Calculating determinant not implement for matrices largerer than 2x2.")
        return det  

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        

    def inverse(self):
    # your code

    def transpose(self):
    # your code

    # Overloaded operators

    def __add__(self,other):
    # your code

    def __sub__(self,other):
    # your code

    def __mul__(self,other):
    # your code