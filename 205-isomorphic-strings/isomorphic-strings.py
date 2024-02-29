class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # for i in range(len(s)):
        #     if s[i] == t[i]:
        #         return True
        #     if s[i] in d:
        #         if d[s[i]]!=t[i]:
        #             return False
        #         else:
        #             return True
        #     else:
        #         d[s[i]] = t[i]

        map1 = []
        map2 = []
        for idx in s:
            map1.append(s.index(idx))
            #print(map1)
        for idx in t:
            map2.append(t.index(idx))
        if map1 == map2:
            return True
        return False
