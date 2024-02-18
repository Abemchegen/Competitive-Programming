class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:


        pre = nums[:]

        pre.reverse()
        pre.append(0)
        pre.reverse()

        for i in range(1, len(pre)):

            pre[i]  += pre[i-1]

        print(pre)

        ans = [0] * (len(nums))
        
        for i in range(len(nums)):

            ans[i] = ((nums[i] * i) - pre[i] ) +  pre[-1] - pre[i + 1]  - (nums[i] * (len(nums) - 1 - i))

        return ans

        