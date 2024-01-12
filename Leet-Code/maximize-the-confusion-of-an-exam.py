class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:

        def maxcon(char):
            maxi = 0
            left = 0
            count = 0

            for i in range(len(answerKey)):
                if answerKey[i] == char:
                    count+= 1

                while count > k:
                    if answerKey[left]== char:
                        count-= 1
                    left+= 1

                maxi = max(maxi, i-left+1)

            return maxi

        maxt = maxcon("F")
        maxf = maxcon("T")
        print(maxt, maxf)

        return max(maxt, maxf)
