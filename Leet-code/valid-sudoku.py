class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(len(board)):
            d={}
            for j in range(len(board[0])):
                if board[i][j]!=".":
                    if board[i][j] in d:
                        return False
                    else:
                        d[board[i][j]]=1
           

        for j in range(len(board[0])):
            d={}
            for i in range(len(board)):
                if board[i][j]!=".":
                    if board[i][j] in d:
                        return False
                    else:
                        d[board[i][j]]=1
           
      

        for i in range(0,len(board)-2,3):
            
            for j in range(0,len(board[0])-2,3):
                d={}
                for r in range(i,i+3):
                    for c in range(j,j+3):
                        if  board[r][c] !="." and board[r][c]in d:
                            return False
                        else:
                            d[board[r][c]]=1
                   

        return True

                

        