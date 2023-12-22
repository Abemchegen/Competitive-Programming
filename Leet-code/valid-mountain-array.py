class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr)<3:
            return False

        end=0

        for i in range(len(arr)-1):
            if arr[i] >= arr[i+1]:
                end= i
                break
        if end == 0:
            return False

        for i in range(end, len(arr)-1):
            if arr[i]<=arr[i+1]:
                return False
        return True


        