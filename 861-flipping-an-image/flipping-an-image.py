class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:

        i,j=0,0
        for i in range(len(image)):
            image[i] = image[i][::-1]
        #print(image)
        i = 0
        for i in range(len(image)):
            for j in range(len(image)):
                if image[i][j] == 0:
                    image[i][j] = 1
                else:
                    image[i][j] = 0
        return image