class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:

        nums.sort()

        # [-1,1,1,2,4]

        left=0
        right=len(nums)-1
        count=0
        while left < right :

            if nums[left] + nums [right] < target :
                count+=right-left
                left+=1
            
            else:
                right-=1
                
        return count


        