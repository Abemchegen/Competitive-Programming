class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times
        

    def q(self, t: int) -> int:

        left = 0
        right = len(self.times) - 1
        ans = 0

        while left <= right:

            mid = (left + right) // 2

            if self.times[mid] <= t:
                ans = mid
                left = mid + 1

            else:
                right = mid - 1

        c = Counter(self.persons[:ans + 1])
        maxi = max(c, key = lambda x : c.get(x))
        maxi = c[maxi]

        for i in range(ans, -1, -1):

            if c[self.persons[i]] == maxi:
                return self.persons[i]

        

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)