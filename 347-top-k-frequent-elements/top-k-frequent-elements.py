class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        x = Counter(nums)
        print(x)
        c=0
        b=[]
        x.values()
        #print(x.most_common()[0][0])
        for i in range(k):
            b.append(x.most_common()[i][0])
        return b
        
        