class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:

        m=[]

        for i,j in enumerate(s):
            m+=[[indices[i],j]]
        m.sort()
        ans=""
        for i in m:
            ans+=i[1]
        return ans
        
