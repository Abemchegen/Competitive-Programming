class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:


       a = bisect_right(letters, target)
      
       return letters[a] if a < len(letters) else letters[0]
