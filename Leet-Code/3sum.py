class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        ans=set()

        nums.sort()

        for i in range(len(nums)-2):

            left=i+1
            right=len(nums)-1
           
            while left < right :

                tot=nums[i] + nums[left] + nums[right]
            
                if tot == 0 :
                    ans.add((nums[i], nums[left], nums[right])) 
                    left+=1
                    right-=1     

                elif tot > 0 :
                    right-=1
                else:
                    left+=1

        return list(ans)

                


        