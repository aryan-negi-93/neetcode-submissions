class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        obj = {}

        for elm in strs:
            order = "".join(sorted(elm))
            if order not in obj:
                obj[order] = []

        for elm in strs:
            order = "".join(sorted(elm))
            if order in obj:
                obj[order].append(elm)

        return list(obj.values())
  











        