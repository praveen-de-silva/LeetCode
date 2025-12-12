class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0]) # no of rows and cols
        dpGrid = [[0] * cols for _ in range(rows)]  # Dynamic Programming table
        dpGrid[0][0] = int(grid[0][0])

        for dx in range(rows):
            for dy in range(cols):
                
                crntVal = grid[dx][dy]

                if dx == 0 and dy == 0:
                    pass
                elif dx == 0 and dy > 0:
                    crntVal += dpGrid[dx][dy-1]
                elif dx > 0 and dy == 0:
                    crntVal += dpGrid[dx-1][dy]
                else:
                    if dpGrid[dx][dy-1] < dpGrid[dx-1][dy]: # same issue
                        crntVal += dpGrid[dx][dy-1]
                    else:
                        crntVal += dpGrid[dx-1][dy]

                dpGrid[dx][dy] = crntVal
  
        return dpGrid[rows-1][cols-1]
