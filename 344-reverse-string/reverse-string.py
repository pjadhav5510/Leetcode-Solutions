class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i,j = 0,len(s)-1
        x=""
        for i in range(len(s)//2):
            x = s[j]
            s[j] = s[i]
            s[i] = x
            print(s[i])
            j-=1
            print(j)
        print(s)