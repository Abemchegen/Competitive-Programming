class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        ans = []
        bucket = []

        def backtrack(i):

            if i >= len(nums):
                ans.append(bucket[:])
                return 
            
            

            for j in range(len(nums)):
                
                if not bucket or (bucket and nums[j] not in bucket):
                    
                    bucket.append(nums[j])
                    backtrack(i+1)
                    bucket.pop()


        backtrack(0)
               
        return ans



        