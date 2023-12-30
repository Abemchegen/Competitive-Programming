class Solution:
    def sortSentence(self, s: str) -> str:

        li=s.split()

        ans=[0]*len(li)

        for i in range(len(li)):
            ans[int(li[i][-1])-1]= li[i][0:len(li[i])-1]
        ans=" ".join(ans)

        return ans
            
        