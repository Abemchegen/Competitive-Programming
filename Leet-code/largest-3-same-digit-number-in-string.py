class Solution:
    def largestGoodInteger(self, num: str) -> str:
        
        ans=[]
        for i in range(2, len(num)):
            if(num[i]==num[i-1]==num[i-2]):
                ans.append(num[i]*3)
        ans.sort()
        
        return ans[-1] if ans else ""