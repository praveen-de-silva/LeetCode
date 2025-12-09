class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = list()
        n = len(s)
        pars = {'(':')', '{':'}', '[':']'}

        for ch in s:
            if ch in pars:
                stack.append(ch)
            elif len(stack) > 0 and pars[stack.pop()] == ch: # need to check: ch in pars.values() if s contains other chars than parentheses
                continue
            else:
                return False
        return len(stack) == 0
