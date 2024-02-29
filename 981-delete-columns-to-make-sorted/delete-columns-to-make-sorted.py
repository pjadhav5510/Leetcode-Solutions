class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        
        c = 0

        if len(strs[0])== 1:
            for i in range(1,len(strs)):
                if strs[i-1] > strs[i]:
                    c+=1
        else:
            for i in range(len(strs[0])):
                for j in range(1,len(strs)):
                    if strs[j-1][i] > strs[j][i]:
                        print(strs[j-1][i],'  ',strs[j][i])
                        c+=1
                        break

        
        return c