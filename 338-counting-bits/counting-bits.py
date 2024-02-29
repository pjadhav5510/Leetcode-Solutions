class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0]*(n+1)

        for i in range(n+1):
            x = bin(i).replace("0b", "")
            print(x)
            x = Counter(x)
            print(x)
            dp[i] = x['1']
        return dp