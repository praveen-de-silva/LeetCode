class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        countApples = sum(apple)
        capacity.sort()
        
        i = len(capacity)-1
        countBoxes = 0

        while i>=0 and countApples > 0:
            countApples -= capacity[i]
            countBoxes += 1
            i -= 1

        return countBoxes

        
        
