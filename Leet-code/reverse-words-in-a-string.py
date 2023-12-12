class Solution:
    def reverseWords(self, s: str) -> str:

        li=list(s.split())
        li=li[::-1]
        return " ".join(li)
        