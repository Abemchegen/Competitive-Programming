class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:

        a = [i for i in range(len(tickets))]
        q = deque(a)
        count = 0

        while q:

            a = q.popleft()
            tickets[a] -= 1
            count += 1

            if tickets[a] != 0:
                q.append(a)

            else:
                if a == k :
                    break

        return count




            
        