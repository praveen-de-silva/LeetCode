# ---------
# Method 01
# ---------
# Time compexity = O(n^2)

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        n = len(events)
        events.sort()
        
        vals = [0] * n

        

        for i in range(n):
            j = i+1
            while j < n and events[j][0] <= events[i][1]:
                j += 1

            maxVal = 0
            if j < n:
                for k in range(j, n):
                    maxVal = max(maxVal, events[k][2])
            maxVal += events[i][2]
            vals[i] = maxVal
        # print(events)
        # print(vals)
        return max(vals)
        
