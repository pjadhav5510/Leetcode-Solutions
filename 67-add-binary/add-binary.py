class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x = int("".join(str(x) for x in a), 2)
        y = int("".join(str(x) for x in b), 2)
        z = x+y

        return bin(z).replace('0b','')
        