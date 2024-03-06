class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def possible (rate):
            hours = 0
            for i in range(len(piles)):

                hours += ceil(piles[i]/ rate)

            return hours <= h

        left = 1
        right = max(piles)

        while left < right :

            mid = (right + left) // 2
            x = possible(mid)

            if x:
                right = mid             
            else:
                left  = mid + 1

        return right

        