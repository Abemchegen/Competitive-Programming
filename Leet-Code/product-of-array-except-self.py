class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        before=[1]
        after=[1]
        total=1

        for i in range(len(nums)):
            total*=nums[i]
            before.append(total)
        before.pop()
    
        total=1

        for i in range(len(nums)-1, -1, -1):
            total*=nums[i]
            after.append(total)
        after.pop()
        after.reverse()

        output=[]
        for i in range(len(before)):
            output.append(before[i]*after[i])
        return output

        