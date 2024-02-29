class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:

        x = ''
        b = set()
        for i in emails:
            i = i.split('@')
            for j in range(len(i[0])):
                if i[0][j] == '.':
                    continue
                elif i[0][j] == '+':
                    break
                else:
                    x += i[0][j]
            x = x+'@'+i[1]
            b.add(x)
            x = ''
        #b = set(b)
        return len(b)