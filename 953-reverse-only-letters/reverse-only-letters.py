class Solution:
    def reverseOnlyLetters(self, s: str) -> str:

        x,a = [],[]
        y,b = [],[]
        for i in range(len(s)):
            if s[i].isalpha():
                x.append(s[i])
                a.append(i)
            else:
                y.append(s[i])
                b.append(i)
        print(x,a)
        x = x[::-1]

        i=0
        c,d = 0,0
        t=list(s)
        for i in range(len(s)):
            if s[i].isalpha():
                t[i]= x[c]
                c+=1
            else:
                print(i)
                t[i]= y[d]
                d+=1
        return ''.join(t)