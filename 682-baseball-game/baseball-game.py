class Solution:
    def calPoints(self, operations: List[str]) -> int:

        s = []
        c=0
        for i in range(len(operations)):
            if operations[i] == 'D':
                x = int(s[c-1])
                x*=2
                s.append(x)
                c+=1
            elif operations[i] == 'C':
                s.pop()
                c-=1
            elif operations[i] == '+':
                x = int(s[c-1]) + int(s[c-2])
                s.append(x)
                c+=1
            else:
                s.append(int(operations[i]))
                c +=1
            print(s)
            print(c)
        c=0
        for i in s:
            c +=i

        return c
