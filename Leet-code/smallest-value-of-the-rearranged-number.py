class Solution:
    def smallestNumber(self, num: int) -> int:

        s=list(str(num))
        s.sort()
        
        if s[0]=="0" and len(s)>1:
            j=1
            for i in range(len(s)):
                if s[i]!="0":
                    j=i
                    break   
            s[0],s[j]=s[j],s[0]
            s=int("".join(s))
        elif s[0]=="-" :
            ans=s[len(s):0:-1]
            ans="".join(ans)
            s=int(ans)*-1
        else:
            s=int("".join(s))
        return s




        