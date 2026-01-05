class Solution:
    def maxMatrixSum(self, matrix):
        total = 0
        neg = 0
        mini = float('inf')

        for row in matrix:
            for val in row:
                if val < 0:
                    neg += 1
                total += abs(val)
                mini = min(mini, abs(val))

        # if count of the negative numbers is even then there will be all positive. Otherwise the minimum will be got the minus value.
        if neg % 2 == 1:
            total -= 2 * mini

        return total
