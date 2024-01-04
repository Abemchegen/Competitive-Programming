class Solution:
    
    def removeDuplicates(self, nums: List[int]) -> int:

        duplicate=0
        unique=1
        ans=1

        while unique < len (nums):
            if nums[unique]==nums[duplicate]:
                unique+=1
            else:
                ans+=1
                duplicate+=1
                print(nums[duplicate])
                nums[duplicate]=nums[unique]
                
                unique+=1
        return ans






        