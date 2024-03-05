class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        ans = []
        bucket = []
        nums.sort()

        def backtrack(i):

            
            ans.append(bucket[:])

            for j in range(i, len(nums)):

                if j > i and nums[j] == nums[j-1]:
                    continue
                bucket.append(nums[j])
                backtrack(j+1)
                bucket.pop()

        backtrack(0)
        return ans




        