class Solution:
    def findPoisonedDuration(self, ts: List[int], d: int) -> int:

        c = 0

        for i in range(len(ts)):

            if i < len(ts)-1:
                if ts[i] + d - 1 < ts[i+1]:
                    c += d
                else:
                    c += ts[i+1] - ts[i]
            else:
                c +=d
        return c