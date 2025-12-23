class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        n = len(events)
        events.sort()
        print(events)
        vals = [0] * n

        

        for i in range(n):
            j = i+1
            maxVal
            
            while j < n and events[j][0] <= events[i][0]:
                j += 1

            if j == n:
                continue

            

            for k in range(j, n):

        
        return 4
        
