class Solution:
    def canPlaceFlowers(self, fb: List[int], n: int) -> bool:
        c=0
        fb=[0]+fb+[0]
        for i in range(1,len(fb)-1):
            if fb[i-1] == 0 and fb[i+1] == 0 and fb[i] == 0:
                fb[i] += 1
                c +=1
            # if i-1 == 0 and fb[i-1] == 0 and fb[i] == 0:
            #     fb[i-1] += 1
            #     c +=1
            # if i+2 == len(fb) and fb[i] == 0 and fb[i+1] == 0:
            #     fb[i-1] += 1
            #     c +=1
        
        if c >=n:
            return True
        else:
            return False