import random


class Matrix:

    def __init__(self, rows, cols):
        self.grid = [[None]*cols for _ in range(rows)]
        self.row_count = rows
        self.col_count = cols

    def create_matrix(self, i=0, j=0):

        if i >= self.row_count and j >= self.col_count:
            return

        if self.grid[i][j] is None:
            self.grid[i][j] = int(input("enter for (" + str(i) + "," + str(j) + ") "))
        else:
            return

        if j < self.col_count - 1:
            self.create_matrix(i, j + 1)

        if i < self.row_count - 1:
            self.create_matrix(i + 1, 0)





