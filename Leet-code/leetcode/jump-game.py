class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        curr =  0
        
        for i in range(len(nums)):

            if i == len(nums) - 1 :
                return True
                
            curr = max(curr - 1, nums[i])

            if curr <= 0 :
                return False

        return True
        


