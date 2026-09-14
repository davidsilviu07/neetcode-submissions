class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()        # caracterele din fereastra curentă
        left = 0            # marginea din stânga a ferestrei
        best = 0            # cea mai mare lungime găsită

        for right in range(len(s)):
            # cât timp caracterul curent e deja în fereastră,
            # scot din stânga până dispare duplicatul
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            # acum fereastra e validă: adaug caracterul curent
            seen.add(s[right])

            # actualizez maximul (lungimea ferestrei e right - left + 1)
            best = max(best, right - left + 1)

        return best