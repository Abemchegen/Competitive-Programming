class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        first = float("INF")
        last = -1

        left = 0
        right = len(nums) - 1

        while left <= right:

            mid = left + (right - left) // 2

            if nums[mid] == target:

                first = min(first, mid)
                right = mid - 1
                
            elif nums[mid] < target:

                left = mid + 1

            else:
                right = mid - 1

        left = 0
        right = len(nums) - 1

        while left <= right:

            mid = left + (right - left) // 2

            if nums[mid] == target:

                last = max(last, mid)
                left = mid + 1

            elif nums[mid] > target:

                right = mid - 1

            else:
                left = mid + 1

        if first == float("INF"):
            return [-1, -1]
            
        return [first, last]
            

                
        