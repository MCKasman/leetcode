class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.

        You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

        Algorithm

        1. Transpose matrix
        2. Reverse matrix rows
        """
        columns = len(matrix[0])
        rows = columns

        # transpose matrix
        for i in range(columns):
            for j in range(i, rows):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # reverse matrix rows
        for i in range(rows):
            matrix[i].reverse()
