class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:


        b= defaultdict(int)
        

        for i in range(len(bills)):

            b[bills[i]] += 1

            if bills[i] == 10 :
                
                if b[5] > 0:

                    b[5] -= 1
                    
                else:

                    return False
                    
            elif bills[i] == 20:

                if b[10] >= 1 and b[5] >= 1 :

                    b[10] -= 1
                    b[5] -= 1

                elif b[5] >= 3 :
                    b[5] -= 3
                    
                else:
                    return False

        return True 




        