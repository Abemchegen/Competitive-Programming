class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        valid=[]
        nums.sort()
        for i in range(len(nums)-2):
            if nums[i]+nums[i+1]>nums[i+2] and nums[i]+nums[i+2]>nums[i+1] and nums[i+1] + nums[i+2]>nums[i]:
                valid.append(nums[i] + nums[i+1] +nums[i+2])
        
        valid.sort()
        return valid[-1] if valid else 0
        
        