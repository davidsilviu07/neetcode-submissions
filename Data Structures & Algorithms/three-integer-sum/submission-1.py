class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()                 # sortăm ca să putem folosi doi pointeri
        result = []
        n = len(nums)

        for i in range(n):
            # sar peste valori duplicate pentru primul element al tripletei
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # dacă nums[i] > 0, cum array-ul e sortat, restul sunt și mai mari
            # => suma nu mai poate fi 0
            if nums[i] > 0:
                break

            left, right = i + 1, n - 1   # cei doi pointeri, imediat după i și la capăt

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1            # suma prea mică => mutăm left dreapta
                elif total > 0:
                    right -= 1           # suma prea mare => mutăm right stânga
                else:
                    # am găsit o tripletă care dă 0
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # sar peste duplicate pentru left și right
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return result