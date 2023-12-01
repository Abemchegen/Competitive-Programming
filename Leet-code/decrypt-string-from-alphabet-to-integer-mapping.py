class Solution:
    def freqAlphabets(self, s: str) -> str:
        
        i=len(s)-1
        ans=""

        while i>=0:
            if s[i]=="#":
                i-=2
                a=s[i]
                i+=1
                a+=s[i]
                i-=1
                ans+=chr(int(a)+96)
            else:
                ans+=chr(int(s[i])+96)
            i-=1
        return "".join(reversed(ans))
                



