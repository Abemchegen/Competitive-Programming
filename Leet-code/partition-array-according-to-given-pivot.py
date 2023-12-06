class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less=[]
        more=[]
        p=0
        for i in range(len(nums)):
            if nums[i]<pivot:
                less.append(nums[i])
            elif nums[i]>pivot:
                more.append(nums[i])
            else:
                p+=1
        return less+[pivot]*p+more
        