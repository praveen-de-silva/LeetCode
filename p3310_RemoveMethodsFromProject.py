class Solution(object):
    def remainingMethods(self, n, k, invocations):
        """
        :type n: int
        :type k: int
        :type invocations: List[List[int]]
        :rtype: List[int]
        """
        # --- create graph ---
        g = [[] for _ in range(n)] 

        for u, v in invocations:
            g[u].append(v)

        # --- find all suspicious nodes ---
        susp = set()
        stack = [k]

        while stack:
            m = stack.pop()

            if m in susp:
                continue
            
            susp.add(m)

            for adj_m in g[m]:
                if adj_m not in susp:
                    stack.append(adj_m)

        # --- final return ---
        for u, v in invocations:
            if u not in susp and v in susp:
                return list(range(n))

        return [i for i in range(n) if i not in susp]

        
        
