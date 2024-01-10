class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        ans=[]

        sd=Counter(s[:len(p)])
        pd=Counter(p)

        if sd==pd:
            ans.append(0)

        print(pd)
        for i in range(len(p),len(s)):
            sd[s[i-len(p)]]-=1
            sd[s[i]]+=1
          
            if sd[s[i-len(p)]]==0:
                del sd[s[i-len(p)]]

            print(sd)
            if sd==pd:
                ans.append(i-len(p)+1)

        
        return ans





        