class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:


        d = Counter(nums)

        f = defaultdict(int)

        left = 0 
        ans = 0
        for i in range(len(nums)):

            f[nums[i]] += 1

            while len(f) == len(d) :
              
                ans += len(nums) - i 

                f[nums[left]] -= 1

                if f[nums[left]] == 0 :
                    del f[nums[left]]
                left += 1

        return ans



        