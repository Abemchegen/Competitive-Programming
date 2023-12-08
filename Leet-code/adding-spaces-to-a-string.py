class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans=""
        j=0
        for i, t in enumerate(s):
            if j<len(spaces) and i==spaces[j]:
                ans+=" "
                j+=1
            ans+=t
        return ans
            
        