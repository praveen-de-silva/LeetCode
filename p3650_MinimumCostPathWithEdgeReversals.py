from typing import List
import heapq

class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        for u, v, w in edges:
            g[u].append((v, w))       # u -> v costs w
            g[v].append((u, 2 * w))   # v -> u costs 2w

        INF = 10**18
        dist = [INF] * n
        dist[0] = 0
        pq = [(0, 0)]

        while pq:
            cost, node = heapq.heappop(pq)
            if cost != dist[node]:
                continue
            if node == n - 1:
                return cost

            for nxt, w in g[node]:
                nc = cost + w
                if nc < dist[nxt]:
                    dist[nxt] = nc
                    heapq.heappush(pq, (nc, nxt))

        return -1
