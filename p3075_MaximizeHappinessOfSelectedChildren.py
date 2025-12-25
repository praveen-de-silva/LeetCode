class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort()
        n = len(happiness)
        result = happiness[-1]

        for i in range(1, k):
            crnt = happiness[n-1-i] - i
            if crnt < 0:
                crnt = 0
            result += crnt

        return result
