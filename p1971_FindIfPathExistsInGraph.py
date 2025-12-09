# ---------
# Method 01
# ---------

class Solution(object):
    def validPath(self, n, edges, source, destination):
        parents = list(range(n))
        rank = [1]*n # for indicate the depth of the tree
        
        def findLeader(s):
            ''' find the leader of the set which include 's' '''
            while parents[s] != s:
                parents[s] = parents[parents[s]]
                s = parents[s]
            return s

        def unionSet(a, b):
            ''' change parents according to the sets; easy to check union '''
            la, lb = findLeader(a), findLeader(b)

            if la == lb:
                return

            if rank[la] < rank[lb]:
                parents[la] = lb
            else:
                parents[lb] = la

                if rank[la] == rank[lb]:
                    rank[la] += 1

        for u, v in edges:
            unionSet(u, v)

        print(parents)
                
        return findLeader(source) == findLeader(destination)

# ---------------
# Method 02 : DFS
# ---------------

from collections import defaultdict

def validPath(n, edges, source, destination):
    seen = set()
    
    # --- make the graph ---
    graph = defaultdict(list)

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # --- define dfs ---
    def dfs(s):
        if s == destination:
            return True
        
        if s in seen:
            return
        seen.add(s)
        
        for adj in graph[s]:
            if adj not in seen:
                if dfs(adj):
                    return True
        return False
            
    return dfs(source)





if __name__ == '__main__':
    edges = [
        [0,1],[0,2],[1,3],[2,3]
    ]

    print(validPath(4, edges, 0, 1))

# ---------------
# Method 03 : BFS
# ---------------

from collections import deque

def getGraph(n, edges):
    graph = {i : [] for i in range(n)}

    for u, v in edges:
        graph[u] = graph.get(u, []) + [v]
        graph[v] = graph.get(v, []) + [u]

    return graph

def validPath(n, edges, source, destination):
    graph = getGraph(n, edges)
    seen = set()
    q = deque({source})

    while q:
        crnt = q.popleft()

        if crnt in seen:
            continue

        seen.add(crnt)

        if crnt == destination:
            print(seen, graph)
            return True
        
        for adj in graph[crnt]:
            if adj in seen:
                continue

            q.append(adj)

    return False





if __name__ == '__main__':
    edges = [
        [0,1],[0,2],[3,5],[5,4],[4,3]
    ]

    print(validPath(3, edges, 3, 5))
