from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        visited = set()
        maxArea = 0

        def dfsVisit(s):
            nonlocal maxArea
            visited.add(s)
            q = deque()
            q.append(s)
            crntArea = 0

            while q:
                crntNode = q.popleft()
                crntArea += 1
                maxArea = max(maxArea, crntArea)
                
                for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                    adjX, adjY = crntNode[0]+dx, crntNode[1]+dy

                    # check validity
                    if adjX >= n or adjX < 0 or adjY >= m or adjY < 0:
                        continue

                    if grid[adjX][adjY] == 1 and (adjX, adjY) not in visited:
                        q.append((adjX, adjY))
                        visited.add((adjX, adjY))

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and (i, j) not in visited:
                    dfsVisit((i,j))

        return maxArea




        
