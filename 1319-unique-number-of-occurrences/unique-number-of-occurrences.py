class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        b = Counter(arr)
        x = []
        x.append(b.values())
        print(len(x[0]))
        b = set(x[0])
        print(b)

        if len(x[0]) == len(b):
            return True
        