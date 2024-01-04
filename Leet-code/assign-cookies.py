class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        ptr=0
        count=0
        for i in range(len(g)):
            
            while ptr<len(s) and s[ptr]<g[i] :
                ptr+=1

            if ptr < len(s) and s[ptr]>=g[i]:
                count+=1
                ptr+=1
            if ptr == len(s):
                break



        return count

             


        