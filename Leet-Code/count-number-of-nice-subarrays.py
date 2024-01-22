class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        ans=0
        left=0
        count=0
        temp=0
        for i in range(len(nums)):

            if nums[i] % 2 != 0 :
                count+=1
                temp=0

            while count == k :
               

                if nums[left] % 2 !=0 :
                    count-=1
                left+=1
                temp+=1
            print(ans)
            ans+=temp

        return ans