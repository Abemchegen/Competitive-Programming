class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:

        right=defaultdict(int)
        left=defaultdict(int)

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                right[i-j]+=mat[i][j]
                left[i+j]+=mat[i][j]

        mid=0
        if len(mat)%2!=0:
            mid=mat[len(mat)//2][len(mat)//2]

        return right[0]+left[len(mat)-1]-mid