class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:


        def possible(num):

            day = 0
            a = 0

            for i in range(len(weights)):
                
                if a + weights[i] <= num:
                    a += weights[i]
                else:
                    day += 1
                    a = weights[i]
                    if a > num:
                        return False
            day += 1
            return day <= days

        left = sum(weights) // days 
        right = max(weights) * (ceil(len(weights) / days))

        out = right

        while left <= right:

            mid = left + (right - left) // 2

            if possible(mid) :
                
                out = min(out, mid)
                right = mid - 1

            else :
                left = mid + 1


        return out
    





                

        