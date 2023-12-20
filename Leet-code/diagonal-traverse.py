class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        ans=[]
        d=defaultdict(list)

        for r in range(len(mat)):
            for c in range(len(mat[0])):
                d[r+c]+=[mat[r][c]]

        for i in d:
            if i%2==0:
                d[i].reverse()
            ans+=d[i]
        return ans
            

                


            




        