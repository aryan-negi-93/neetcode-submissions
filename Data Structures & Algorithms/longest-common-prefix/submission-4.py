class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        result = ""
        prefix = ""
        for i in range(len(strs[0])):
            prefix = strs[0][:i+1]
            for j in range(1,len(strs)):

                if prefix != strs[j][:i+1]:
                    result += prefix
                    return result[:-1]
        result += prefix

        return result



        