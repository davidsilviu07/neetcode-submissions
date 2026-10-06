class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        rez = [[]]
        for x in nums:
            noi = [s + [x] for s in rez]
            rez += noi
        return rez