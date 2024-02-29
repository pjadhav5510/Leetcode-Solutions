class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [0]*(n+1)

        if n == 0:
            return 0
        if n ==1 or n==2:
            return 1
        if len(dp) > 3:
            dp[1] = 1
            dp[2] = 1
            for i in range(3,len(dp)):
                dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
        return dp[-1]  