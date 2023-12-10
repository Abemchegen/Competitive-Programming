class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
    
        d={}
        for index, path in enumerate(paths):
            files=path.split()
            folder=files[0]

            for file in range(1,len(files)):
                title,content=files[file].split("(")
                content=content[:-1]
                if content in d:
                    d[content].append(folder + "/" + title)
                else:
                    d[content]=[folder + "/" + title]
        ans=[]
        for i in d:
            if len(d[i])>1:
                ans.append(d[i])
        return ans
        
        
                

       

        