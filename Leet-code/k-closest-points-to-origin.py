class Solution:
    def customsort(self, point: List[int])-> int:
        return math.sqrt((point[0]-0)**2 + (point[1]-0)**2)

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        points.sort(key=self.customsort)
        
        ans=points[:k]

        return ans



        