class NumArray:

    def __init__(self, nums: List[int]):
        self.P=[0]
        for x in nums:

            self.P.append(self.P[-1]+x)

    def sumRange(self, left: int, right: int) -> int:
        return self.P[right+1]-self.P[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)