class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        
        r1,r2=[],[]
        c=0
        for i in s:
            if i in '(': 
                c +=1
                r1.append(i)
                if c ==1:
                    r1.pop()
            if i in ')':
                c -=1
                r1.append(i)
                if c==0:
                    r1.pop()
        return "".join(r1)