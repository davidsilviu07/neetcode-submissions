class Solution:
    def sortColors(self, nums: List[int]) -> None:
        zero = 0
        i = 0
        high = len(nums) - 1

        while i <= high:
            if nums[i] == 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1
                i += 1
            elif nums[i] == 1:
                i += 1
            else:
                nums[i], nums[high] = nums[high], nums[i]
                high -= 1