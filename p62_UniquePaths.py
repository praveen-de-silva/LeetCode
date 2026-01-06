class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        paths = {}

        def countPaths(i, j):
            if (i,j) == (m-1, n-1):
                return 1
            if i == m or j == n:
                return 0
            if (i,j) in paths:
                return paths[(i,j)]
            crntPaths = countPaths(i+1,j) + countPaths(i,j+1)
            paths[(i,j)] = crntPaths
            return crntPaths

        return countPaths(0,0)
        
