class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        d=defaultdict(int)

        left=0
        longest=0
        for i in range(len(fruits)) :

            d[fruits[i]]+=1

            while len(d) > 2 :
                d[fruits[left]]-=1

                if d[fruits[left]]==0:
                    del d[fruits[left]]
            
                left+=1

            longest=max(longest, i-left+1)

        return longest