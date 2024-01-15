class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        left=0
        total=0
        minlength=float("INF")

        for i in range(len(nums)):

            total += nums[i]

            if total >= target :

                while total - nums[left]  >= target :

                    total-=nums[left]
                    left+=1

                minlength= min (minlength, i-left+1)

        return minlength if minlength != float("INF") else 0


        