class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        s = Counter(magazine)
        print(s)
        for i in ransomNote:
            if i in s and s[i] > 0:
                s[i] -=1
                print(s[i])
                continue
            else:
                return False
        return True

        