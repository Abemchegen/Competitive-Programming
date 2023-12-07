class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans=[]
        for i in range(len(boxes)):
            num=0
            for j in range(len(boxes)):
                if i!=j and boxes[j]=="1":
                    num+=abs(j-i)
            ans.append(num)
        return ans
        
        