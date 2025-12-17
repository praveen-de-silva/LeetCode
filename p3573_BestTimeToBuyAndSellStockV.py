from typing import List

class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        INF = 10**18
        
        # dp[t][0]: free
        # dp[t][1]: holding buy
        # dp[t][2]: holding short
        dp = [[-INF]*3 for _ in range(k+1)]
        dp[0][0] = 0
        
        for price in prices:
            new_dp = [row[:] for row in dp]
            for t in range(k+1):
                # start transactions
                new_dp[t][1] = max(new_dp[t][1], dp[t][0] - price)  # buy
                new_dp[t][2] = max(new_dp[t][2], dp[t][0] + price)  # short sell
                
                # finish transactions
                if t < k:
                    new_dp[t+1][0] = max(
                        new_dp[t+1][0],
                        dp[t][1] + price,   # sell
                        dp[t][2] - price    # buy back
                    )
            dp = new_dp
        
        return max(dp[t][0] for t in range(k+1))
