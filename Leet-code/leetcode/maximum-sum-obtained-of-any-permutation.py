class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:

        pre = [0] * (len(nums) + 1)

        for i in range(len(requests)):

            pre[requests[i][0]] += 1
            pre[requests[i][1] + 1] -= 1

        for i in range(1, len(pre)):

            pre[i] += pre[i - 1]

        pre.pop()
       
        pre.sort(reverse = True)
        nums.sort(reverse = True)
        ans = 0

        for i in range(len(nums)):

            if pre[i] == 0 :
                break
            ans += pre[i] * nums[i]

        return ans % (10 ** 9 + 7)