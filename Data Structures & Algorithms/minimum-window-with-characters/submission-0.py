class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        need = {}
        for c in t:
            need[c] = need.get(c, 0) + 1

        need_count = len(need)
        have = 0

        window = {}
        left = 0
        best_len = float("inf")
        best_range = [0, 0]

        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c, 0) + 1

            if c in need and window[c] == need[c]:
                have += 1

            while have == need_count:   # fereastra e validă, o strâng
                if (right - left + 1) < best_len:
                    best_len = right - left + 1
                    best_range = [left, right]

                left_char = s[left]
                window[left_char] -= 1
                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1
                left += 1

        if best_len == float("inf"):
            return ""
        start, end = best_range
        return s[start:end + 1]