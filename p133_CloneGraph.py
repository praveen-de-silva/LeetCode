"""
-----------------------------
Method 01 : BFS (using Queue)
-----------------------------
"""

class Solution(object):

    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if node == None:
            return None
        
        newGraph = Node(node.val) # copy of the graph
        tempNodes = {newGraph.val:newGraph} #  maps all copied nodes
        seen = {node.val:node}
        q = deque([node])

        while q:
            crntNode = q.popleft()

            for adjNode in crntNode.neighbors:
                
                # --- update seen and tempNodes ---
                if seen.get(adjNode.val) is None:
                    q.append(adjNode)
                    seen[adjNode.val] = adjNode
                    
                    newAdjNode = Node(adjNode.val)
                    tempNodes[adjNode.val] = newAdjNode

                # --- update the neighbors of current node ---
                tempNodes[crntNode.val].neighbors.append(tempNodes[adjNode.val])

        return newGraph

"""
------------------------------------
Method 02 : DFS (Recursive Approach)
------------------------------------
"""

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):

    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if node is None:
            return None

        oldToNew = {}

        def clone_DFS(node):
            if node in oldToNew:
                return oldToNew[node]

            copy = Node(node.val)
            oldToNew[node] = copy
            
            for adj in node.neighbors:
                copy.neighbors.append(clone_DFS(adj))

            return copy

        return clone_DFS(node)


        return newGraph
        
