class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:

        colmax = [0] * len(grid[0])

        for i in range(len(grid)):

            for j in range(len(grid[0])):

                colmax[j] = max(colmax[j], grid[i][j])

        ans = 0

        for i in range(len(grid)):

            rowmax = max(grid[i])

            for j in range(len(grid[0])):
                
                inc = min(colmax[j], rowmax) - grid[i][j]
               
                if inc > 0:
                    ans += inc

        return ans










        