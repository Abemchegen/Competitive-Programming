class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        found = False

        for i in range(len(nums)) :

            num = len(nums) * 2
            neg = False
            

            if nums[i] < 0 :

                neg = True

            j = (nums[i] + i) % len(nums)

            if i != j :

                while num:

                    if (neg and nums[j] > 0) or (not neg and nums[j] < 0) :

                        break
                 
                    j = (j + nums[j]) % len(nums)
                    
                    if j == i :

                        found = True
                        break
                    num -= 1
            if found :
                break

        return found




       


        
        