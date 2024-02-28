class Solution:
    def maxSubArray(self, nums: List[int]) -> int:


        total = nums[0]

        ans = total

        for i in range(1, len(nums)):

            if total < 0:

                total = nums[i]
            
            else:

                total += nums[i]

            ans = max(total, ans)

        return ans




            


        