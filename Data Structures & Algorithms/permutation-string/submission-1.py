class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1=Counter(s1)
        lun=len(s1)
        r=0
        while r+lun<=len(s2):
            c2=Counter(s2[r:r+lun])
            if c1==c2:
                return True
            r=r+1
        return False
