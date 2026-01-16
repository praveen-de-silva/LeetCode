# ---------
# Method 01 
# ---------

# 502 / 648 testcases passed

class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        hFences.extend([1,m])
        vFences.extend([1,n])
        hFences.sort()
        vFences.sort()

        hDiff = []
        vDiff = []

        for i in range(len(hFences)):
            for j in range(i+1,len(hFences)):
                hDiff.append(abs(hFences[i]-hFences[j]))

        for i in range(len(vFences)):
            for j in range(i+1,len(vFences)):
                vDiff.append(abs(vFences[i]-vFences[j]))

        hDiff.sort()
        vDiff.sort()

        side = -1

        for i in range(len(hDiff)):
            for j in range(len(vDiff)):
                if hDiff[i] == vDiff[j] and side < hDiff[i]:
                    side = hDiff[i]

        if side == -1:
            return -1
        return (side * side) % (10**9 + 7)

# ---------
# Method 02 
# ---------

# Passed all test cases

class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        hFences.extend([1,m])
        vFences.extend([1,n])
        hFences.sort()
        vFences.sort()
        hDiff = set()
        vDiff = set()

        for i in range(len(hFences)):
            for j in range(i+1,len(hFences)):
                hDiff.add(abs(hFences[i]-hFences[j]))

        for i in range(len(vFences)):
            for j in range(i+1,len(vFences)):
                vDiff.add(abs(vFences[i]-vFences[j]))

        sides = list(hDiff.intersection(vDiff))
        sides.sort()

        if len(sides)==0:
            return -1
        return (sides[-1]**2) % (10**9 + 7)    
