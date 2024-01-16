class NumArray:

    def __init__(self, nums: List[int]):
        self.nums=nums
        self.prefix=[0]
        self.total=0

        for i in self.nums:
            self.total+=i
            self.prefix.append(self.total)

        print(self.prefix)

    def sumRange(self, left: int, right: int) -> int:

        return self.prefix[right+1] - self.prefix[left]

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)