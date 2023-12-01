class Solution:
    def average(self, salary: List[int]) -> float:

        mini=min(salary)
        maxi=max(salary)
        ans=sum(salary)-maxi-mini
        return ans/(len(salary)-2)
        