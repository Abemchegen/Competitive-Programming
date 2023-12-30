class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        d={}

        

        another=nums[:]
        nums.sort()
        

        for i in range(len(nums)-1,-1,-1):
            d[nums[i]]=i
        print(d)

        ans=[]
        for i in another:
            ans.append(d[i])
        return ans