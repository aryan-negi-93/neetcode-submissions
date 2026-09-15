class Solution:
    def maxArea(self, heights: List[int]) -> int:

        n = len(heights)
        i = 0
        j = n - 1
        maximum  = 0

        while i < j:
            width = j - i
            min_wall = min(heights[i] , heights[j])
            water = width * min_wall
            if water > maximum:
                maximum = water
            elif heights[i] <= heights[j]:
                i+=1
            elif heights[i] >= heights[j]:
                j-=1

        return  maximum





        