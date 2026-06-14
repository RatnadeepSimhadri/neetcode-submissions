class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        og_color = image[sr][sc]
        if og_color == color:
            return image
        Solution.fill(image,sr,sc,color,og_color)
        return image


    @staticmethod
    def fill(image:List[List[int]],r:int, c:int, color:int, og_color: int):
        image[r][c] = color 

        # Check all OG Color Neighbors that haven't been colored and fill the color 
        for neighbor in [(1,0),(-1,0),(0,1),(0,-1)]:
            _r = r + neighbor[0]
            _c = c + neighbor[1]

            if 0 <= _r < len(image) and 0 <= _c < len(image[0]) and image[_r][_c] ==  og_color:
                Solution.fill(image,_r,_c,color,og_color)

        
        


        
