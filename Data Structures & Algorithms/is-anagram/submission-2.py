class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hsMap1, hsMap2 = {} , {}
        for c in s:
            if c not in hsMap1:
                hsMap1[c] = 1
            else:
                hsMap1[c] += 1
        
        for c in t:
            if c not in hsMap2:
                hsMap2[c] = 1
            else:
                hsMap2[c] += 1
        
        if hsMap1 == hsMap2:
            print(hsMap1)
            print(hsMap2)
            return True
        
        else:
            print(hsMap1)
            print(hsMap2)
            return False