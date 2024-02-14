class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        board = [["e" for _ in range(n)] for _ in range(m)]

        for i in guards :

            board[i[0]][i[1]] = "g"

        for i in walls:

            board[i[0]][i[1]] = "w"

        

        for i in range(m):

            c=0
            guard=False

            for j in range(n):

                c+=1

                if guard and board[i][j] == "e":
                    board[i][j] = "m"

                elif board[i][j] == "g":
                    for b in range(j-1,j-c,-1):
                        if board[i][b] == "e":
                         board[i][b] = "m"
                    guard=True
                    c=0

                elif board[i][j] == "w":
                    guard=False
                    c=0
    
        for j in range(n):

            c=0
            guard=False

            for i in range(m):

                c+=1

                if guard and board[i][j] == "e":
                    board[i][j] = "m"

                elif board[i][j] == "g":
                    for b in range(i,i-c,-1):
                        if board[b][j] == "e":
                           board[b][j] = "m"
                    guard=True
                    c=0

                elif board[i][j] == "w":
                    
                    guard=False
                    c=0
        
        ans=0
        for i in range(m):
            for j in range(n):
                if board[i][j] == "e":
                    ans+=1

        return ans
        