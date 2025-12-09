class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        graph = dict()
        center = int()
        i = 0 # to prevent long run

        # --------------
        # make the graph
        # --------------

        for u,v in edges:
            if i > 10:
                break

            if v in graph.get(u, []): # check whether u-v exisits (avoid duplicate edges)
                continue    
            
            graph[u] = graph.get(u, []) + [v]
            graph[v] = graph.get(v, []) + [u]
            
            i += 1
        
        # ---------------------
        # check the center node
        # ---------------------

        size = len(graph.keys()) # size of the graph

        for u, neighbours in graph.items():
            if len(neighbours) == size - 1:
                center = u
                
        return center
