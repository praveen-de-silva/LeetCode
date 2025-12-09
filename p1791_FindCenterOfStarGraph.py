class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        guess = edges[0]

        for edge in edges:
            if len(guess) == 1:
                break
            
            for node in guess:
                if node not in edge:
                    guess.remove(node)
                
        return guess[0]
