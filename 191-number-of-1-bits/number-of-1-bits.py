class Solution:
    def hammingWeight(self, n: int) -> int:

        n = bin(n).replace('0b','')
        c = Counter(n)
        return c['1']