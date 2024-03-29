class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:


        for i in range(len(matrix)):

            if matrix[i][-1] >= target:

                left = 0
                right = len(matrix[i]) - 1

                while left <= right:

                    mid = (right + left ) // 2

                    if matrix[i][mid] == target:
                        return True

                    elif matrix[i][mid] > target:
                        right = mid - 1
                    
                    else:
                        left = mid + 1

                return False





                



        