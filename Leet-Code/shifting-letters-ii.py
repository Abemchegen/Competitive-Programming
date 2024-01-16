class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:

        prefix=[0]*(len(s)+1)

        for i in range(len(shifts)):

            if shifts[i][2]==0:

                prefix[shifts[i][0]] -= 1
                prefix[shifts[i][1]+1] +=1
             
            else:

                prefix[shifts[i][0]] += 1
                prefix[shifts[i][1]+1] -=1

        for i in range(1,len(prefix)):
            prefix[i]=prefix[i] + prefix[i-1]
        


        s=list(s)

        for i in range(len(s)):

            s[i]=chr(((ord(s[i])+prefix[i]-ord("a"))%26) + ord("a")) 
        
        s= "".join(s)
        return s

        
        
