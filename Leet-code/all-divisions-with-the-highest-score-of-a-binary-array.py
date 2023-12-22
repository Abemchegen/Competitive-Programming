class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:

        total= sum(nums)
    
        left=0
        right=total
        d=defaultdict(list)

        for i in range(len(nums)):
            d[left+right].append(i)
            if nums[i]==0:
                left+=1
            else:
                right-=1
        d[left+right].append(i+1)
        return d[max(d)]


        

            

        




        