class Solution:
    def pivotInteger(self, n: int) -> int:
        a=[]
        for i in range(1,n+1):
            a.append(i)
        print(a)

        l,r = 0,sum(a)
        print(l,r)

        for i in range(len(a)):
            if l + a[i] == r: return a[i]
            l += a[i]
            r -= a[i]
        return -1