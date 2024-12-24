class Solution(object):
    def isValid(self, s):
        brkts = {'(' :')', '{':'}', '[':']'}
        stack = []
        
        for ch in s:
            if ch in brkts:
                stack.append(ch)
            elif len(stack)==0:
                return False
            else:
                stcPop = stack.pop()
                if ch!=brkts[stcPop]:
                    return False

        if len(stack)==0:
            return True
        return False