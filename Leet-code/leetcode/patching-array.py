class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:

        possible = 0
        patches = 0

        for i in range(len(nums)) :
            
            if nums[i] > n:
                break

            while possible < nums[i] - 1 :

                possible += possible + 1
                patches += 1
            
            possible += nums[i]
        
        while possible < n :

                possible += possible + 1
                patches += 1

        return patches


          