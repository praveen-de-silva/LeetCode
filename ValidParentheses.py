class Solution(object):
    def isValid(self, s):
        brkts = {'(' :')', '{':'}', '[':']'}
        queue = []
        
        for ch in s:
            if ch in brkts:
                queue.append(ch)
            elif len(queue)==0:
                return False
            else:
                qPop = queue.pop()
                if ch!=brkts[qPop]:
                    return False
                    
        if len(queue)==0:
            return True
        return False