class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        count=0

        left=0
        curr=0
        maxnum=0
        for i in range(len(nums)):

            if nums[i]==1:
                curr+=1

            elif nums[i]==0:
                count+=1

                if count>1:
                    while count>1 :
                        if nums[left]==1:
                            curr-=1
                        else:
                            count-=1
                        left+=1

            maxnum=max(maxnum, curr)
        maxnum=max(maxnum, curr)

        if count==0 :
            return maxnum-1
        return maxnum




        