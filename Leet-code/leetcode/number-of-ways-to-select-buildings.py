class Solution:
    def numberOfWays(self, s: str) -> int:

        s = list(map(int, s))

        c0 = c1 = c01 = c10 = c010 = c101=  0
       
        for i in range(len(s)):

            if s[i] == 0:
                c0 += 1
                if c1:
                    c10 += c1
                
                if c01:

                    c010 += c01
            else:
                c1 += 1
                if c0:
                    c01 += c0

                if c10:

                    c101 += c10

        return c010 + c101







        