class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        initProfit = 0
        n = len(prices)

        # --- Step 01 : find the initial profit ---
        for i in range(n):
            initProfit += prices[i] * strategy[i]

        # --- Step 02 : find the profit when window at [0:k] ---
        gain = 0

        for i in range(k):
            if i < k//2:
                gain += (0 - strategy[i]) * prices[i]
            else:
                gain += (1 - strategy[i]) * prices[i]

        maxGain = max(0, gain)
        
        # --- Step 03 : find the profit through the array ---
        for i in range(1, n-k+1):
            gain += prices[i+k-1] * (1-strategy[i+k-1]) - prices[i+k//2-1] - prices[i-1] * (0-strategy[i-1])
            if maxGain < gain:
                maxGain = gain

        return initProfit + maxGain
