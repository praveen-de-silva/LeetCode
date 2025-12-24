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

# ---------
# Method 02
# ---------
# Time complexity = O(n*lg(n))

from bisect import bisect_right

class Solution:
    def maxTwoEvents(self, events: list[list[int]]) -> int:
        events.sort()  # Sort by start time
        n = len(events)
        starts = [e[0] for e in events]  # For binary search
        maxFromHere = [0] * n  # max value from i to end
        
        # --- fill maxFromHere from the end ---
        maxFromHere[-1] = events[-1][2]
        for i in range(n-2, -1, -1):
            maxFromHere[i] = max(events[i][2], maxFromHere[i+1])
        
        # --- sequentally find the maximum value ---
        result = 0
        for i in range(n):
            j = bisect_right(starts, events[i][1]) # index after all values <= events[i][1], Time complexity = O(lg(n))
            total = events[i][2] # current value
            if j < n:
                total += maxFromHere[j] # max value in the right side
            result = max(result, total)
        
        return result
