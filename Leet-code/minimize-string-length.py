class Solution:
    def minimizedStringLength(self, s: str) -> int:
        d={}
        ans=0
        for i in range(len(s)):
            if s[i] in d:
                d[s[i]]+=1
            else:
                d[s[i]]=1
        for i in d:
            ans+=1
                
        return ans
        