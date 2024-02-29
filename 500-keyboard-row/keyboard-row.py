class Solution:
    def findWords(self, words: List[str]) -> List[str]:

        ans = []
        a = []
        for i in range(len(words)):
            str1 = words[i].lower()
            for j in range(len(str1)):
                #print(str1)
                if str1[j] in "qwertyuiop":
                    a.append(1)
                elif str1[j] in "asdfghjkl":
                    a.append(2)
                elif str1[j] in "zxcvbnm":
                    a.append(3)
            if len(set(a)) == 1:
                ans.append(words[i])
            a = []
        return ans

        
        