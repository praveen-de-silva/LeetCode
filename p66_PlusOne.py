class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        crnt = 0

        for num in digits:
            crnt *= 10
            crnt += num

        return list(map(int, list(str(crnt + 1))))
