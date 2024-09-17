# [73. Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/)

## $O(m+n)$ Memory Solution

Space Complexity: $O(m+n)$
Time Complextiy: $O(mn)$ 3 times
One for iterating through the matrix,
one for fill in columns,
one for fill in rows.


## $O(1)$ Solution Memory Solution

Time Complextiy: $O(mn)$ 

### AC CODE
```
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        rowZero = False ## If the first row is 0 or not.

        ## Determine which rows or cols need to be 0
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0

                    if r > 0:   
                        matrix[r][0] = 0
                    else:
                        rowZero = True

        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        if matrix[0][0] == 0:
            for r in range(rows):
                matrix[r][0] = 0
        if rowZero:
            for c in range(cols):
                matrix[0][c] = 0
```
