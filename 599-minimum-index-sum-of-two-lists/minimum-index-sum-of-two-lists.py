class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:

        a  = {}
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    a[list1[i]] = i+j
        
        result_keys = [key for key, value in a.items() if value == min(a.values())]
        return result_keys
