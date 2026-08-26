class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        obj1 = {}
        obj2 = {}

        for i in range(len(s)):
            if s[i] not in obj1:
                obj1[s[i]] = 1
            else:
                obj1[s[i]] += 1

        for j in range(len(s)):
            if t[j] not in obj2:
                obj2[t[j]] = 1
            else:
                obj2[t[j]] += 1

        for key , value in obj1.items():
            if key not in t:
                return False
            if obj2[key] != value:
                return False

        return True
            
                

        



        