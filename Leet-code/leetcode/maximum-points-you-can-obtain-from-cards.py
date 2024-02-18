class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:


        d = sum (cardPoints[ : len(cardPoints) - k ])

        total = sum(cardPoints)

        remov = d

        left = 0 
       
        for i in range(len(cardPoints) - k ,  len(cardPoints)):
            
            d -= cardPoints[left]

            left += 1 

            d += cardPoints[i]

            remov = min(remov, d)

        return total - remov


        