class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:

        d = defaultdict(int)

        for i in range(len(intervals)):
            d[intervals[i][0]] = i

        temp = sorted(intervals)

        def bs(curr):
            
            left = curr
            right = len(temp) - 1

            while left <= right:

                mid = (right + left) // 2

                if temp[mid][0] >= temp[curr][1]:
                    right = mid - 1
                else:
                    left = mid + 1

            if left == len(temp) :
                return -1

            return left
        
        ans = [-1] * len(intervals)

        for i in range(len(temp)):

            a = bs(i)
            if a != -1:

                ans[d[temp[i][0]]] = d[temp[a][0]]

        return ans











        








        