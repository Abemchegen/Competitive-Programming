class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if not strs:
            return ""
        
        min_length= min(len(s) for s in strs)

        ans=""

        for i in range(min_length):
            char=strs[0][i]

            if all (s[i]==char for s in strs):
                ans+=char
            else:
                break
        return ans