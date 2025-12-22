class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n, m = len(strs), len(strs[0]) 
        sortedPairs = [False] * (n-1) # if strs[i] <= strs[i+1] (except the last one)
        result = 0 
        
        for j in range(m): 
            for i in range(n-1): 
                if not sortedPairs[i] and strs[i][j] > strs[i+1][j]: 
                    result += 1 
                    break 
            else: 
                for i in range(n-1):
                    if strs[i][j] < strs[i+1][j]:
                        sortedPairs[i] = True
            
        return result
