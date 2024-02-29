class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res = Counter(words[0])
        print("res before for: ",res)
        for i in words:
            res &= Counter(i)
            print("res in for: ",res)
        return list(res.elements())
