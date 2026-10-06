class Solution:
    def rob(self, nums: List[int]) -> int:
        prev2, prev1 = 0, 0          # dp[i-2] și dp[i-1]
        for x in nums:
            prev2, prev1 = prev1, max(prev1, prev2 + x)
        return prev1