class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:

        i,j=0,0
        c=0
        #while j < len(num):
        print(len(str(num)))
        x='1'
        for i in range(k):
            x = x + '0'
        print(x)
        z=num
        while i < len(str(num)):
            j = z%int(x)
            print(j)
            if j == 0:
                z = int(z/10)
            elif num%j == 0:
                c+=1
                z = int(z/10)
            else:
                z = int(z/10)
            print(z)
            i+=1
        return c