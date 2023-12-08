class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ans=set()
        for pair in ranges:
            for i in range(left,right+1):
                if i >= pair[0] and i <= pair[1]:
                    ans.add(i)
        return len(ans)>=right+1-left
            

