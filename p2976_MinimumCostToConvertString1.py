class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        INF = 1e18
        dist = [[INF] * 26 for _ in range(26)]
        for i in range(26):
            dist[i][i] = 0

        for o, c, w in zip(original, changed, cost):
            u = ord(o) - 97
            v = ord(c) - 97
            if w < dist[u][v]:
                dist[u][v] = w

        # Floyd–Warshall
        for k in range(26):
            for i in range(26):
                if dist[i][k] == INF:
                    continue
                ik = dist[i][k]
                for j in range(26):
                    nk = ik + dist[k][j]
                    if nk < dist[i][j]:
                        dist[i][j] = nk
        ans = 0
        for s_ch, t_ch in zip(source, target):
            if s_ch == t_ch:
                continue
            u = ord(s_ch) - 97
            v = ord(t_ch) - 97
            if dist[u][v] == INF:
                return -1
            ans += dist[u][v]
        return ans
