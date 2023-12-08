class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1="qwertyuiop"
        row2="asdfghjkl"
        row3="zxcvbnm"


        ans=[]

        for word in words:
            
            r1=r2=r3=True
            for letter in word:
                if letter.lower() not in row1:
                    r1=False
                    break
            for letter in word:
                if letter.lower() not in row2:
                    r2=False
                    break
            for letter in word:
                if letter.lower() not in row3:
                    r3=False
                    break
            if r1 or r2 or r3:
                ans.append(word)
        return ans
            
