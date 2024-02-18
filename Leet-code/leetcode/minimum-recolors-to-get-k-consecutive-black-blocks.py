class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:

        count = 0 

        for i in range(0, k):

            if blocks[i] == "W":
                count += 1

        maxcount = count
        left = 0

        for i in range(k, len(blocks)):

            if blocks[left] == "W" :
                count -= 1

            left += 1

            if blocks[i] == "W" :
                count += 1

            maxcount = min(maxcount, count )

        return maxcount



        