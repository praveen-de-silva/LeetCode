class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        def BFS(start, end):
            q = deque()
            q.append(start)
            visited = set()
            visited.add(start)
            b = {tuple(p) for p in blocked}

            while q:
                crntNode = q.popleft()
                
                if crntNode == end or len(visited) > 20000:
                    return True 

                for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                    adjX, adjY = crntNode[0]+dx, crntNode[1]+dy
                    
                    if adjX < 0 or adjX >= 1000000 or adjY < 0 or adjY >= 1000000:
                        continue
                    
                    if (adjX, adjY) not in b and (adjX, adjY) not in visited:
                        q.append((adjX, adjY))
                        visited.add((adjX, adjY))
            return False
        return BFS(tuple(source), tuple(target)) and BFS(tuple(target), tuple(source)) 
        
