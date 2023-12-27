class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        same=[]
        nocare=[]
        d={}
        for i in range(len(arr1)):
            if arr1[i] in arr2 :
                same.append(arr1[i])    
            else:
                nocare.append(arr1[i])  

        for i in range(len(arr2)):
            d[arr2[i]]=i

        counting= [0] * len(arr2)

        for i in range(len(same)):
            counting[d[same[i]]]+=1
        
        same=[]

        for i in range(len(counting)):
            
            while(counting[i]):
                same.append(arr2[i])
                counting[i]-=1
        nocare.sort()

        same+=nocare
        return same

        


        
        

    



          
           



