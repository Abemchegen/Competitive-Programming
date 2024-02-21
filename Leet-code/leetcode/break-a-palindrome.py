class Solution:
    def breakPalindrome(self, palindrome: str) -> str:

        ans = list(palindrome)

        c = Counter(palindrome)

        if len(c) == 1 and len(palindrome) == 1:
            return ""
       
        flag = False
        
        for i in range(len(palindrome)) :

            if len(palindrome) % 2 != 0 and i == len(palindrome) // 2 :
                print(palindrome[i])
                continue 

            if palindrome[i] != "a" and not flag :

                ans[i]= "a"
                flag = True

        if not flag:
            ans[-1] = "b"

        ans = "".join(ans)

        
        return ans



        
            



        