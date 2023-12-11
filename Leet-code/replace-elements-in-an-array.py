class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        d={}
        for i in range(len(nums)):
            d[nums[i]]=i
       
        for i in range(len(operations)):
            index=d[operations[i][0]]
            operations[i][0]=index
           
            nums[operations[i][0]]=operations[i][1]

            d[nums[operations[i][0]]]=index
              
        return nums
        