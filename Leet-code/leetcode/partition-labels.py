class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        d = defaultdict(int)

        ans = []

        for i in range(len(s)) :

            d[s[i]] = i

        print(d)

        end = d[s[0]]
        left = 0

        for i in range(len(s)):

            end = max(end, d[s[i]])

            if end == i :

                ans.append(i - left + 1)
                left = i + 1
                end = 0

        return ans



            

           
