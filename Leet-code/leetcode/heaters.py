class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:

        heaters.sort()
        
        def closest(target):

            left = 0
            right = len(heaters) - 1

            while left <= right:

                mid = (right + left) // 2

                if heaters[mid] >= target:

                    right = mid - 1 

                else:
                    left = mid + 1

            if right == -1:
                right = 0
            if left == len(heaters):
                left -= 1

            return min(abs(target - heaters[left]), abs(target - heaters[right]))

        ans = 0
        for i in range(len(houses)):

            ans = max(ans, closest(houses[i]))

        return ans

            


            


        