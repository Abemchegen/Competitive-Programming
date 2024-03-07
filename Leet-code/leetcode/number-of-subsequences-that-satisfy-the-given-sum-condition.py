class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:


        ans = 0
        mod = 1000000007
        nums.sort()

        for i in range(len(nums)):

            right = bisect_right(nums, (target - nums[i]))
            length = right - i

            if length > 0 :
                ans += pow(2, length - 1, mod)

        return ans % mod




        



            


        