class Solution:
    def reverseVowels(self, s: str) -> str:

        i,j = 0,len(s)-1
        s = list(s)
        vowels = ['a','e','i','o','u']
        print(s)

        while i < j:
            if s[i].lower() not in vowels:
                i +=1
            elif s[j].lower() not in vowels:
                j -=1
            else:
                s[i],s[j] = s[j],s[i]
                i+=1
                j-=1
        return ''.join(s)


        
