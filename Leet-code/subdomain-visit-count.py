class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        d={}

        for domain in range(len(cpdomains)):
            l=cpdomains[domain].split()
            li=l[1].split(".")
            a = ""
            for i in range(len(li)):
                a = ".".join(li[i:])
                # print(a)
                if a not in d:
                    d[a]=int(l[0])
                else:
                    d[a] += int(l[0])
                # print(d[i])
        ans=[]
        for i,j in d.items():
            strr=""
            strr+=str(j) + " " + str(i)
            ans.append(strr)
        return ans



                


            
            

        
        