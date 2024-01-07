class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool: 

        i=0
        j=0
        if name[0] != typed[0]:
            return False
        while j < len(typed):
           
            if i <len(name):
                if name[i] == typed[j]:
               
                    i+=1
                    j+=1
                else:
                    if i > 0 and typed[j]!=name[i-1]:
                        return False
                    else:
                        j+=1
            else:
                if typed[j]!=name[-1]:
                    return False
                else:
                    j+=1


        return i==len(name)




        