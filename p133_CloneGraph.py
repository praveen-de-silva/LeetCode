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
        
