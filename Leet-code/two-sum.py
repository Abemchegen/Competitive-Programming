class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        d=defaultdict(list)

        for i in range(len(nums)):
            d[nums[i]].append(i)
        
        nums.sort()

        left=0
        right=len(nums)-1

        while left<right:
            
            if nums[left] + nums[right]==target:
                if nums[left]==nums[right]:
                    return d[nums[left]]
                else:
                    return d[nums[left]]+d[nums[right]]
            else:
                if nums[left] + nums[right] > target:
                    right-=1
                else:
                    left+=1
        return []


        




        