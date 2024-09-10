class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ## Compare the target with the first and last elements in a row
        
        top = 0
        while top < len(matrix):
            
            left, right = 0, len(matrix[0]) - 1
            #print(matrix[top][left], matrix[top][right])
            if (matrix[top][left] == target) or (matrix[top][right] == target):
                return True
            
            
            if matrix[top][left] < target < matrix[top][right]:
                ## Target is either in this row or non-exist
                while left <= right:
                    mid = (left + right) // 2
                    if target == matrix[top][mid]:
                        return True
                    if target < matrix[top][mid]:
                        right = mid - 1
                    else:
                        left = mid + 1
                top += 1
            else:
                top += 1

        return False
