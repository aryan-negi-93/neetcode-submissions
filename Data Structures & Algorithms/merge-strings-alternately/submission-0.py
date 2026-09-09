class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1 = len(word1)
        n2 = len(word2)
        res = ""

        i = 0
        j= 0

        while i < n1 and j < n2:
            res += word1[i]
            res += word2[i]
            i+=1
            j+=1

        print(i , "=" , j)
        if i < n1:
            res+=word1[i:]
        elif j < n2:
            res+= word2[j:]
        
        return res






        