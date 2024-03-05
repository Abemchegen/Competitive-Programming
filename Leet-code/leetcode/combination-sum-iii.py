class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:


        nums = [i+1 for i in range(9)]
        ans = []
        bucket = []

        def backtrack(i):

            if sum(bucket)>= n or i >= len(nums):
               
                if sum(bucket) == n and len(bucket) == k:
                    ans.append(bucket[:])
                return

            for j in range(i, len(nums)):

                # if nums[j] in bucket:
                #     continue
                bucket.append(nums[j])
                backtrack(j+1)
                bucket.pop()

        backtrack(0)
        return ans
        