class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        return words== sorted(words, key= lambda word: [order.index(word[i]) for i in range(len(word))])

       

        