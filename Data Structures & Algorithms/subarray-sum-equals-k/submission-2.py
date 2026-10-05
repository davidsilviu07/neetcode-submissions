class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        vazute = {0: 1}
        prefix = 0
        rez = 0
        for x in nums:
            prefix += x
            rez += vazute.get(prefix - k, 0)
            vazute[prefix] = vazute.get(prefix, 0) + 1
        return rez