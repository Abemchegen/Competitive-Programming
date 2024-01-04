class Solution:
    def dividePlayers(self, skill: List[int]) -> int:

        skill.sort()

        left=0
        right=len(skill)-1

        s= s=skill[0]+skill[-1]

        chemistry=0
        while left<right:
            if s==skill[left]+skill[right]:
                chemistry+=skill[left]*skill[right]
                left+=1
                right-=1
            else:
                chemistry=-1
                break
        return chemistry

        