class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:

        i=0
        j=n
        ans=[]
        while(j<len(nums)):
            ans+=[nums[i],nums[j]]
            i+=1
            j+=1
        return ans



        