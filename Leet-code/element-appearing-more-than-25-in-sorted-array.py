class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:

        d=Counter(arr)
        maxi=0
        for key in d:
            if d[key] > d[maxi]:
                maxi = key
        return maxi
        