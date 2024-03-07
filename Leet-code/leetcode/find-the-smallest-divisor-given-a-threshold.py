class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        def division(mid):
            ans = 0  

            for i in range(len(nums)):

                ans += ceil(nums[i] / mid)

            return ans

        left = 1
        right = max(nums)

        while left < right :

            mid = (right + left ) // 2
            
            if division(mid) <= threshold:

                right = mid

            else:
                left = mid + 1


        return right

            

                

        