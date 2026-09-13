class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        best = 0

        while left < right:
            # aria curentă: lățime × înălțimea barei mai scunde
            width = right - left
            height = min(heights[left], heights[right])
            best = max(best, width * height)

            # mut pointerul care arată spre bara mai scundă
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return best