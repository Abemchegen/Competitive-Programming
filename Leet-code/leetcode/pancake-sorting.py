class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:

        sor = sorted(arr , reverse = True)
        ans = []

        i = 0
        j = len(arr)

        for _ in range(len(arr) - 1) :
            
            ans.append(arr.index(sor[i]) + 1)
            ans.append(j)
           
            left = 0 
            right = arr.index(sor[i])

            while left < right :

                arr[left] , arr[right] = arr[right] , arr[left]
                left += 1
                right -= 1

            left = 0 
            right = j - 1

            while left < right :
                arr[left] , arr[right] = arr[right], arr[left]
                left += 1
                right -= 1

            j -= 1
            i += 1


        return ans






        