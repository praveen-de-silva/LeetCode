# ----------------------
# Method 01(i) : Topdown
# ----------------------

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        mem = {}

        def getCoinsCount(bal):
            if bal == 0:
                return 0
            if bal < 0:
                return float('inf')

            if bal in mem:
                return mem[bal]
            
            minCount = float('inf')
            for coin in coins:  
                tempCount = getCoinsCount(bal-coin) + 1
                minCount = min(minCount, tempCount)
            mem[bal] = minCount
            return minCount

        result = getCoinsCount(amount)

        if result > 1e4:
            return -1
        return result

# ----------------------------------
# Method 01(ii) : Topdown - improved
# ----------------------------------

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        @lru_cache(NoneZ)
        def getCoinsCount(bal):
            if bal == 0:
                return 0
            if bal < 0:
                return float('inf')
            return min(getCoinsCount(bal-c) + 1 for c in coins)

        result = getCoinsCount(amount)

        if result > 1e4:
            return -1
        return result

