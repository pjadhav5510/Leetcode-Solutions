class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:

        flatten = []
        a = []
        for row in mat:
            for num in row:
                flatten.append(num)

        print(flatten)
        if len(mat)*len(mat[0]) != r*c:
            return mat
        else:
            for i in range(r):
                a.append(flatten[i*c:i*c+c])
            return a
        
       