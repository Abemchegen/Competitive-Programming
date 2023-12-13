class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:

        nope=set()
        yup=set()
        for i in range(len(fronts)):
            if fronts[i]==backs[i]:
                nope.add(fronts[i])

        for i in range(len(fronts)):
            
            if fronts[i] not in nope:
                yup.add(fronts[i])
            if backs[i] not in nope:
                yup.add(backs[i])
        return min(yup) if yup else 0

        