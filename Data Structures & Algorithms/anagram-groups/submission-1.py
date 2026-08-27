class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        map = {}

        for elm in strs:
            elm = "".join(sorted(elm))
            if elm not in map:
                map[elm] = []


        for elements in strs:
            elm = "".join(sorted(elements))
            if elm not in map:
                continue
            else:
                map[elm].append(elements)

        return list(map.values())











        