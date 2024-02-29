class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        x,y = [],[]
        for i in s:
            if i == '#':
                if len(x):
                    x.pop()
            else:
                x.append(i)
        for i in t:
            if i == '#':
                if len(y):
                    y.pop()
            else:
                y.append(i)
        
        if x == y:
            return True 
        else:
            return False