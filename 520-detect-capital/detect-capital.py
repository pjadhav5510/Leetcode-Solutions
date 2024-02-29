class Solution:
    def detectCapitalUse(self, s: str) -> bool:

        return s.isupper() or s.islower() or s[0].isupper() and s[1:].islower()
