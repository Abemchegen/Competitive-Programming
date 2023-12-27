class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        for i in range(len(names)):
            smallest=i
            for j in range(i,len(names)):
                if heights[j] > heights[smallest]:
                    smallest = j
            heights[i],heights[smallest]=heights[smallest],heights[i]
            names[i],names[smallest]=names[smallest],names[i]
        return names