# coding:utf-8
# Implementing a Matrix Class
# In this project you will implement a Matrix class in Python. 
# Specifically, you will implement the following methods:
import math
from math import sqrt
import numbers



def zeroes(height, width):
    """    
    Creates a matrix of zeroes.
    """
    g = [[0.0 for _ in range(width)] for __ in range(height)]
    return Matrix(g)

def idensity(n):
    """
    Creates a n x n idensity matrix.
    """
    I = zeroes(n, n)
    for i in range(n):
        I.g[i][i] = 1.0
    return I
   



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
        # TODO 异常 非常规输入处理
        if not self.is_square():
            raise(
                ValueError, "Cannot calculate the trace of a non-square matrix.")
        # TODO Calculates the main diagonal num's sum
        sum = 0
        for i in range(self.h):
            sum += self[i][i]

        return sum     


    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        # TODO
        # detA
        if not self.is_square():
            raise(
                ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(
                NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

        mD = self.determinant()
        if self.h == 1:
            if self.g[0][0] = 0:
                raise(NotImplementedError,
                    "The 1x1 Matrix contains 0 can't inverse")
            else:
                return [[1 / self.g[0][0]]]       
        for i in range(self.h): # Calculates the inverse of a 2x2 Matrix.
            my_Matrix = zeroes(2, 2)
            my_Matrix.g[1][1] = self.g[0][0] / mD
            my_Matrix.g[0][0] = self.g[1][1] / mD
            my_Matrix.g[0][1] = - self.g[0][1] / mD
            my_Matrix.g[1][0] = - self.g[1][0] / mD
            return my_Matrix

        # trace A
        # 与矩阵TraceA * I identity 单位矩阵

    # the matrix is or not a square matrix
    def is_square(self):
        return self.h = self.w    
   
    def transpose(self):
    # your code
    # matrix 的转置 矩阵的行列互换
        my_Matrix = zeroes(self.w, self.h)
        for i in range(self.h):
            for j in range(self.w):
                my_Matrix[j][i] = self[i][j]
        return my_Matrix
            
            
    # Overloaded operators

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise (ValueError,
                   "Matrices can only be added if the dimensions are the same")
            #
        # TODO - your code here
        #
        my_add = zeroes(self.h, self.w)
        for i in range(self.h):
            for j in range(self.w):
                my_add.g[i][j] = self.g[i][j] + other.g[i][j]

        return my_add


    def __sub__(self,other):
         """
        Defines the behavior of - operator (as subtraction)
        """
        #
        # TODO - your code here
        #
        my_sub = zeroes(self.h, self.w)
        for i in range(self.h):
            for j in range(self.w):
                my_sub.g[i][j] = self.g[i][j] - other.g[i][j]

        return my_sub

    def __mul__(self,other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        # 
        # 注意矩阵的A的列 与 相乘矩阵B的行必须相等，才能进行运算
        height = 0
        width = 0
        if isinstance(other, list): # 判断other是否是矩阵，即list形式的矩阵
            height = len(other)
            width  = len(other[0])
        else:
            # 如果是对象，则直接获取行列值
            height = other.h
            width  = other.w


        my_mul = zeroes(self.h, self.w)
        if self.w == height: # 两个矩阵的行列值需要相等 才能相乘
            for i in range(self.h):
                for j in range(width):
                    my_sum = 0
                    for k in range(height):
                        if isinstance(other, list):
                            my_sum += self.g[i][k] * other[k][j]
                            # 通过3个循环变量取所有矩阵的行列值
                        else:
                            my_sum += self.g[i][k] * other.g[k][j]
                        my_mul[i][j] = my_sum
            return my_mul    
        else:
            return NotImplementedError

    # TODO is_square fun implement

    for i in range(self.h):
        for j in range(self.w):
            my_mul[i][j] = ZA