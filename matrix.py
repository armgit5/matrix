import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        # TODO - your code here
        if self.w == 1 or self.h == 1:
            return self.g[0][0]
        if self.w == 2 or self.h == 2:
            a = self.g[0][0]
            b = self.g[0][1]
            c = self.g[1][0]
            d = self.g[1][1]
            return a*d-b*c

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        # TODO - your code here
        sum = 0
        for r in range(self.h):
            for c in range(self.w):
                if r == c:
                    sum += self.g[r][c]
        return sum

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

        # TODO - your code here
        inverse = [[0 for _ in range(self.w)] for _ in range(self.h)]
        
        if self.h == 1 or self.w == 1:
            inverse[0][0] = 1./self.g[0][0]
        if self.h == 2 or self.w == 2:
            a = self.g[0][0]
            b = self.g[0][1]
            c = self.g[1][0]
            d = self.g[1][1]
            adbc = 1/(a*d-b*c)
            inverse[0][0] = d*adbc
            inverse[0][1] = -b*adbc
            inverse[1][0] = -c*adbc
            inverse[1][1] = a*adbc

        return Matrix(inverse)
    
    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
        matrix_transpose = []
        for c in range(self.w):
            row = []
            for r in range(self.h):
                row.append(self.g[r][c])
            matrix_transpose.append(row)

        return Matrix(matrix_transpose)

    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        #   
        # TODO - your code here
        #
        matrixSum = []
        row = []

        for r in range(self.h):
            for c in range(self.w):           
                row.append(self.g[r][c] + other[r][c])
            matrixSum.append(row)
            row = []
    
        return Matrix(matrixSum)

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #   
        # TODO - your code here
        #
        
        matrixNeg = []
        row = []

        for r in range(self.h):
            for c in range(self.w):           
                row.append(-self.g[r][c])
            matrixNeg.append(row)
            row = []
    
        return Matrix(matrixNeg)

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        #   
        # TODO - your code here
        #
        matrixSub = []
        row = []

        for r in range(self.h):
            for c in range(self.w):           
                row.append(self.g[r][c] - other.g[r][c])
            matrixSub.append(row)
            row = []
    
        return Matrix(matrixSub)

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #   
        # TODO - your code here
        #
        def dot_product(vector_one, vector_two):
            sum = 0
            for i in range(len(vector_one)):
                sum += vector_one[i] * vector_two[i]
            return sum
        
        product = []
        mBT = other.T()
        for ra in range(self.h):
            dotP = []
            for rb in range(mBT.h):
                dotP.append(dot_product(self.g[ra], mBT[rb]))
            product.append(dotP)

        return Matrix(product)

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            #   
            # TODO - your code here
            #
            rmul = []
            for r in range(self.h):
                row = []
                for c in range(self.w):
                    row.append(self.g[r][c] * other)
                rmul.append(row)
            return Matrix(rmul)
            