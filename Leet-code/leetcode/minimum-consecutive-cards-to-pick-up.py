class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:


        d = {}

        ans = float("INF")

        for i in range(len(cards)):

            if cards[i] in d :

                ans = min(ans, i - d[cards[i]] + 1)

            d[cards[i]] = i
            

        return ans if ans != float("INF") else -1


        