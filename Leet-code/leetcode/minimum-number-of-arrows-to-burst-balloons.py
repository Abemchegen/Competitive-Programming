class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort( key = lambda x : x[1])
        print(points)

        ans = 1
        arr= points[0][1]
        for i in range(1, len(points)):

            if points[i][0] > arr:

                ans +=1
                arr = points[i][1]

        return ans




