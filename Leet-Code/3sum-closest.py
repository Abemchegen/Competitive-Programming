class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        closest= float ("-INF")

        for i in range(len(nums)-2):

            left=i+1
            right=len(nums)-1

            while left < right :

                tot= nums[i] + nums[left] + nums[right]

                if abs(tot-target) < abs(closest - target):
                    closest= tot

                if tot == target:
                    return tot

                elif tot > target :
                    right-=1
                else:
                    left+=1
                    
        return closest 