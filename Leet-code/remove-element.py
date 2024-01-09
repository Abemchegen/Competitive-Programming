class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left=0
        right=0
        count=0
        while right < len (nums) :
            if nums[right] != val :
                nums [ left], nums[right] = nums [right], nums[left]
                left+=1
                count+=1
            right+=1
        return count