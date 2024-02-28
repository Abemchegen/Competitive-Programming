class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        if rowIndex == 0 :
            return [1]

        ans = self.getRow( rowIndex - 1)
        new = [1]

        for j in range(len(ans) - 1):

            new.append(ans[j] + ans[j + 1])

        new.append(1)

        return new
        