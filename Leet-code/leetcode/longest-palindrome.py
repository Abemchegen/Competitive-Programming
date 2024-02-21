class Solution:
    def longestPalindrome(self, s: str) -> int:

        c = Counter(s)
        
        odd  = False
        ans = 0

        if len(c) == 1:

            return len(s)
            
        for i, val in c.items():

            if val % 2 == 0 :
                ans += val

            else:
                odd = True
                ans += val -1


        if odd:
            ans += 1
        return ans







        