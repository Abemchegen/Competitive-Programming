class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        d = Counter(s1)

        f = Counter(s2[:len(s1)])

        
        left = 0 

        for i in range(len(s1), len(s2)):

            if f == d:
                return True

            else:
                
                f[s2[left]] -= 1

                if f[s2[left]] == 0:
                    del f[s2[left]]

                left += 1
                f[s2[i]] += 1
                print(f)
                
        if f == d:
                return True
        return False

             
        