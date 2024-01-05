class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i=0
        j=0
        out=[]
        while i < len(firstList) and j < len(secondList):
            if firstList[i][0]>= secondList[j][0] and firstList[i][0] <= secondList[j][1]:
              
                if firstList[i][1]>= secondList[j][0] and firstList[i][1] <= secondList[j][1]:
                    out.append([firstList [i][0], firstList[i][1]])

                elif secondList[j][1] >= firstList[i][0] and secondList[j][1] <= firstList[i][1]:
                    out.append([firstList [i][0], secondList[j][1]])
            elif secondList[j][0] >= firstList[i][0] and secondList[j][0] <= firstList[i][1]:

                if firstList[i][1]>= secondList[j][0] and firstList[i][1] <= secondList[j][1]:
                    out.append([secondList [j][0], firstList[i][1]])

                elif secondList[j][1] >= firstList[i][0] and secondList[j][1] <= firstList[i][1]:
                    out.append([secondList [j][0], secondList[j][1]])
            
            if firstList[i][1] < secondList[j][1]:
                i+=1
            else:
                j+=1
        return out




        