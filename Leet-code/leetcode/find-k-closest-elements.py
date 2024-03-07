class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        def bs():

            left = 0
            right = len(arr) - 1

            while left <= right:

                mid = (right + left) // 2

                if arr[mid] == x :
                    return mid

                if arr[mid] > x :
                    right = mid - 1

                else:
                    left = mid + 1

                return -1

        a = bs()

        if a != -1:

            left = a - 1
            right = a + 1
            k -= 1
            
        else:
            a = bisect_left(arr, x)
            left = a - 1
            right = a
 
        while left > -1 and right < len(arr) and k:

            if abs(arr[left] - x) <= abs(arr[right] - x):
                left -= 1
            
            else:
                right += 1

            k -= 1 

        if k:

            if left > -1 :
                left -= k
            
            elif right < len(arr):
                right += k

        left += 1
   
        return arr[left: right]







        





        