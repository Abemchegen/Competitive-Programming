class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        less=float("INF")
        mid=float("INF")
        

        for i in range(len(nums)):
            
            less=min(less, nums[i])

            if nums[i]>mid:
                return True
            if nums[i]>less:
                mid=nums[i]
        return False
        