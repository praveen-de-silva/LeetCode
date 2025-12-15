# --------------------------------
# Method 01 : More space optimized
# --------------------------------

class Solution:
    def func(self, n: int) -> int:
        res = 0
        for i in range(n+1):
            res += i
        return res

    def getDescentPeriods(self, prices: List[int]) -> int:
        n = len(prices)
        pCount = 0
        p, q = 0, 0 # 2 pointers 

        for i in range(n):
            if i+1 < n and (prices[i] == prices[i+1]+1) :
                q += 1
            else:
                pCount += self.func(q-p+1)
                if i+1 == n:
                    break
                q += 1
                p = q
        
        return pCount


# -------------------------------
# Method 02 : More time optimized
# -------------------------------

# * used triangle number concept

class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        n = len(prices)
        pCount = 0
        p = 0 

        for i in range(n):
            if i+1 < n and (prices[i] == prices[i+1]+1) :
                pCount += i-p+2
            else:
                pCount += 1               
                p = i+1
        
        return pCount
