class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        s = s.lower()
        print(s)

        i,j = 0,len(s)-1
        c=0

        for i in range(int(len(s)/2)):
            if s[i] == s[j]:
                print(s[i])
                c+=1 
            j -=1
        
        if c == int(len(s)/2):
            return True
        else:
            return False