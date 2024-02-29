class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        m1 = []
        m2 = []

        t = s.split(" ")
        for i in pattern:
            m1.append(pattern.index(i))
        for j in t:
            m2.append(t.index(j))
        print(m1,m2)
        if m1 == m2:
            return True