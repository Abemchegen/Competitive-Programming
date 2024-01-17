class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        
        leftprefix=[]
        rightprefix=[]
        total=0
        for i in range(len(nums)):
            total+=nums[i]
            leftprefix.append(total)
        total=0
        for i in range(len(nums)-1, -1, -1 ):
            total+=nums[i]
            rightprefix.append(total)
        rightprefix.reverse()

        for i in range(len(leftprefix)):
            if leftprefix[i]==rightprefix[i]:
                return i
        return -1