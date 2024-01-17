class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:

        for i in range(1,len(nums)):
            nums[i]=nums[i] + nums[i-1]
        d=defaultdict(int)
        total=0
        d[0]=1
        for i in range(len(nums)):
            if nums[i] % k in d:
                total+=d[nums[i] % k]
            d[nums[i] % k] += 1
        return total