class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c=Counter(nums)
        ans=[]
        for i,j in c.items():
            if j>len(nums)/3:
                ans+=[i]
        return ans
    
        