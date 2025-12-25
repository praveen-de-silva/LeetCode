class Solution:
    def fib(self, n: int) -> int:
        if n in [0,1]:
            return n

        if n < 0:
            return None # Error!

        return self.fib(n-1) + self.fib(n-2)
