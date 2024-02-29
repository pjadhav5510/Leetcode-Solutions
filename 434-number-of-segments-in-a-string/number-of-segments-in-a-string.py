class Solution:
    def countSegments(self, s: str) -> int:

        x = s.strip(" ")
        x = x.split(" ")
        print(x)
        if s == "" or x[0] == '':
            return 0
        c=0
        #x = list(x)
        for i in range(len(x)):
            if x[i] != '':
                c+=1
        return c
        