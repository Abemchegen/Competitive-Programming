class Solution:
    def printVertically(self, s: str) -> List[str]:
       
        li=s.split()
        ans=[]
        l=len(max(li, key=len))

        for i in range(l):
            temp=[]
            for word in li:
                if i<len(word):
                    temp.append(word[i])
                else:
                    temp.append(" ")
            ans.append("".join(temp))
        for i in range(len(ans)):
            ans[i]=ans[i].rstrip()
        return ans
        
        



            

        

        