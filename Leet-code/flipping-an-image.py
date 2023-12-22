class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:

        for a in image:
            a.reverse()

            for i in range(len(a)):
                if a[i]==1:
                    a[i]=0
                else:
                    a[i]=1
        return image


