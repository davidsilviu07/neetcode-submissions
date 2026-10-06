class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l < r:
            k = (l + r) // 2
            ore = 0
            for p in piles:
                ore += (p + k - 1) // k
            if ore <= h:
                r = k
            else:
                l = k + 1
        return l