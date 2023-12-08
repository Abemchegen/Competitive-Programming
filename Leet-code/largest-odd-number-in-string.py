class Solution:
    def largestOddNumber(self, num: str) -> str:
        s=""
        i=len(num)-1
        while i>=0:
            if int(num[i]) % 2 !=0:
                s=num[:i+1]
                break
            i-=1
        return s
            


        





        return ans[-1]

        