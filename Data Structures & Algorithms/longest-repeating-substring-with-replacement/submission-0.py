class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        best = 0
        max_freq = 0        # cea mai mare frecvență văzută în orice fereastră

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            max_freq = max(max_freq, count[s[right]])

            # dacă fereastra cere mai mult de k schimbări, o strâng
            if (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1

            best = max(best, right - left + 1)

        return best