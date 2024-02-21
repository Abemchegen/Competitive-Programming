class Solution:
    def numRabbits(self, answers: List[int]) -> int:

        c = Counter(answers)
        ans = 0

        for similar, rab in c.items():

            multi = similar + 1

            if similar == 0:
                continue

            if rab % multi == 0:

                ans += rab

            else:

                ans += rab +  multi - (rab % multi)

        return ans + c[0]




            








            
        return ans 
        