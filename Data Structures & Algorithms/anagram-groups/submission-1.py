class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grupuri=defaultdict(list)
        for cuv in strs:
            cheie="".join(sorted(cuv))
            grupuri[cheie].append(cuv)
        return list(grupuri.values())
        