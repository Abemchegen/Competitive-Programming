class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        for i in range(1, len(nums)):

            nums[i] += nums[i - 1]

        d = {0: 1}
        ans = 0

        for i in range(len(nums)):

            if nums[i] - goal in d:
                
                ans += d[nums[i] - goal]

            d[nums[i]] = d.get(nums[i], 0) + 1

        return ans