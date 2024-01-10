class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left=0
        maxlen=0
        d=defaultdict(int)
        for i in range(len(s)):
            d[s[i]]+=1

            while d[s[i]] > 1 :
                d[s[left]]-=1
                left+=1
            maxlen=max(maxlen, i-left+1)

        return maxlen





        