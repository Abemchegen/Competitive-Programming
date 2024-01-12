class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        myset={"a","e","i","o","u"}

        left=0
        count=0
        maxcount=0

        for i in range(len(s)):

            if s[i] in myset:
                print(s[i])
                count+=1
            
            if i-left+1 == k :
                maxcount=max(maxcount, count)
                if s[left] in myset:
                 count-=1
                left+=1
        return maxcount

        