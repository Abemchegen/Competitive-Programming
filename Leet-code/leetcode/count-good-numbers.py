class Solution:
    def countGoodNumbers(self, n: int) -> int:

        # if n == 0:
        #     return 1

        # ans = self.countGoodNumbers(n - 1)

        # if n % 2 != 0:
        #     ans *= 5

        # else:
        #     ans *= 4

        # return ans % (10 ** 9 + 7)

        return ((pow(4, (n // 2) , (1000000007))) * (pow(5, math.ceil(n/2) , (1000000007)))) % (1000000007)