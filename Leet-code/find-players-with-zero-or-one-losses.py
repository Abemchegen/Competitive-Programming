class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loser={}
        ans=[]
        first=set()
        second=set()
        for pair in matches:
            if pair[1] not in loser:
                loser[pair[1]]=1
            else:
                loser[pair[1]]+=1
        for pair in matches:
            if pair[0] not in loser:
                first.add(pair[0])
            if loser[pair[1]]==1:
                second.add(pair[1])
        ans=ans+[sorted(list(first))]+[sorted(list(second))]
        return ans
        



        