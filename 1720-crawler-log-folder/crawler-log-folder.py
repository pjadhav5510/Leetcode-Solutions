class Solution:
    def minOperations(self, logs: List[str]) -> int:
        #print(logs[0].split('/'))
        x=[]
        c=0
        for i in range(len(logs)):
            x = logs[i].split('/')
            if x[0] == '..':
                if c==0:
                    c=0
                else:
                    c-=1
            elif x[0] == '.':
                c = c
            else:
                c+=1
        return c