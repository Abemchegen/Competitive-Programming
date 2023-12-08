class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        ans=[]
        for i, word in enumerate(list1):
            for j, word2 in enumerate(list2):
                if word==word2:
                    ans+=[[word, i+j]]
        ans.sort(key=lambda x : x[1])
        out=[ans[0][0]]
        for i in range(1, len(ans)):
            if ans[i][1]==ans[0][1]:
                out+=[ans[i][0]]
        return out



        

        