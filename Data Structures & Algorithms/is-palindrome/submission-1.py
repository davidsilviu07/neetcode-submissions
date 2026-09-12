class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            # sar peste caracterele non-alfanumerice din stânga
            while left < right and not s[left].isalnum():
                left += 1
            # sar peste caracterele non-alfanumerice din dreapta
            while left < right and not s[right].isalnum():
                right -= 1

            # compar case-insensitive
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True