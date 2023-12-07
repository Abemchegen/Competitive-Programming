class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos=[]
        neg=[]
        ans=[]
        for i in nums:
            if i>=0:
                pos.append(i)
            else:
                neg.append(i)
        for i in range(len(pos)):
            ans+=[pos[i]]
            ans+=[neg[i]]
        return ans


        