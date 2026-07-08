class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
        Understand- given an array of heights, choose any two bars to form a container, 
                    and return the maximum amount of water a container can store.
                input - heights array
                output - Maximum amount of water a container can store
        Plan-
            Using two pointers, start at left and right
            area formula is (width * height )
            width formula is right pointer - left pointer
            keep track of max area as we are going to eventually return it 

            psuedo-
                max area = 0
                set left to 0
                set right to end of heights array

                while left < right:
                    width = right - left
                    height = min(heights[left], heights[right])
                    we want the minimum height as the height of the container so it doesnt tip over
                    find max area
                    move the pointer that points to the shorter height because that is whats used to find area

                return max area at the end
        Implement-
        '''

        max_area = 0
        left = 0
        right = len(heights) - 1

        while left < right:
            width = right - left
            height = min(heights[left], heights[right])
            max_area = max((height * width), max_area) # the formula for area is height * width 
            
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max_area