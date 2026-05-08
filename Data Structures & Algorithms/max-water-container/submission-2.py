class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area, l, r = 0, 0, len(heights)-1

        while l < r:
            min_bar = min(heights[l], heights[r])
            area = (r-l) * min_bar
            if area > max_area:
                max_area = area
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return max_area
        