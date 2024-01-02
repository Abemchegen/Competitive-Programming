class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:

        tasks.sort(reverse=True)
        processorTime.sort()

        ans=0
        print(tasks)
        print(processorTime)
        
        j=0
        for i in range(len(processorTime)):
            ans=max(ans,max(processorTime[i]+tasks[j],processorTime[i]+tasks[j+1],processorTime[i]+tasks[j+2],processorTime[i]+tasks[j+3]))
            j+=4
            print(ans)
        return ans


        
        