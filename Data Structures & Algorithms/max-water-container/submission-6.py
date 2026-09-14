class Solution:
    def maxArea(self, heights: List[int]) -> int:

        n = len(heights)
        i = 0
        j = n - 1
        maximum  = 0

        while i < j:
            min_val = min(heights[i] , heights[j])
            width =  j - i
            water = min_val * width 
            if water > maximum:
                maximum = water
            elif heights[i] >= heights[j]:
                j-=1
            elif heights[i] <= heights[j]:
                i+=1
            
        return maximum
            






    


            




        