class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:

        i=0
        b=[]
        x,c = 999999,0
        while i < len(blocks):
            b.append(blocks[i])

            if len(b) == k:
                for j in b:
                    if j == 'W':
                        c+=1
                x = min(x,c)
                c=0
                b.pop(0)
            i+=1
        return x
        