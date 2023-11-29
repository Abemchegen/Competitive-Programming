class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        
        i= n
        ans=-1
        while i<=2*n:
            if i %2==0 and i%n==0:
                ans= i
                break
            i+=1

        return ans


