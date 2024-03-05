class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        bucket = []

        def backtrack(i):

            if sum(bucket) > target:
                return 
  
            if sum(bucket) == target:
                if bucket not in ans:
                    ans.append(bucket[:])
                return 

            for j in range(i, len(candidates)):
                
                bucket.append(candidates[j])
                backtrack(j)
                bucket.pop()

        backtrack(0)

        return ans





        