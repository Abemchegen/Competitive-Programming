class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        ans = []
        bucket = []

        def backtrack(i):


            ans.append(bucket[:])

            for j in range(i, len(nums)):

                bucket.append(nums[j])
                backtrack(j + 1)
                bucket.pop()

        backtrack(0)
        return list(ans)







        