class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
       
        ans=0
        s=0
        for i in range(len(flips)):
            s=max(s,flips[i])
            if s == i+1:
                ans+=1
        return ans

