class Solution:
    def maxScore(self, s: str) -> int:

        a=s.count("1")
        b=0
        maxi=0

        for i in range(len(s)-1):

            if s[i]=="0":
                b+=1
            else:
                a-=1

            maxi=max(maxi, a+b )

        return maxi