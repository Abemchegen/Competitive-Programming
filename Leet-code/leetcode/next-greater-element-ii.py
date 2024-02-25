class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:


        st = []
        n = len(nums)
        ans = [-1] * n

        for i in range(2 * len(nums)):

            while st and nums[i % n] > nums[st[-1]]:

                ans[st[-1]] = nums[i % n]
                st.pop()

            st.append(i% n)
        
        return ans
        