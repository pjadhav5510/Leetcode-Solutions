class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        c = ""
        for i in range(min(len(word1),len(word2))):
            c += word1[i]
            c+= word2[i]
        
        if int(len(c)/2) == len(word1):
            c += word2[len(word1):]
        elif int(len(c)/2) == len(word2):
            c += word1[len(word2):]
        
        return c