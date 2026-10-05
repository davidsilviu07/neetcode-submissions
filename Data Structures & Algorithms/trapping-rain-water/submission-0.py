class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        total = 0

        l = 0
        bazin = 0
        for r in range(1, n):
            if height[r] >= height[l]:
                total += bazin
                bazin = 0
                l = r
            else:
                bazin += height[l] - height[r]

        stop = l
        r = n - 1
        bazin = 0
        for i in range(n - 2, stop - 1, -1):
            if height[i] >= height[r]:
                total += bazin
                bazin = 0
                r = i
            else:
                bazin += height[r] - height[i]

        return total