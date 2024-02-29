class Solution:
    def reverseWords(self, s: str) -> str:

        s = s.split()
        print(s)
        j = len(s)-1
        for i in range(len(s)//2):
            temp = s[i]
            s[i] = s[j]
            s[j] = temp
            j -=1

        return ' '.join(s)