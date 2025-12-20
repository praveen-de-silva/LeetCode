class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        rows, cols = len(strs), len(strs[0])
        result = 0

        for idy in range(cols):
            crntOrd = 0
            for idx in range(rows):
                tempOrd = ord(strs[idx][idy])

                if tempOrd < crntOrd:
                    result += 1
                    break

                crntOrd = tempOrd

        return result
