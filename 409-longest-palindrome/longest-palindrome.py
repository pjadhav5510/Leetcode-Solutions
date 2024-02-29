class Solution:
    def longestPalindrome(self, s: str) -> int:

        x = Counter(s)
        ans = 0
        for i in x.values():
            ans = ans + ((i // 2) * 2)
            if ans%2 == 0 and i %2 != 0:
                ans += 1
        return ans


        
        