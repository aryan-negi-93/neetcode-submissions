class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        i = 0
        while i < len(arr):
            j = i + 1
            max_elm = -1
            while j < len(arr):
                if arr[j] > max_elm:
                    max_elm = arr[j]
                    
                if i == (len(arr) -1):
                    max_elm = -1
                j+=1
            arr[i] = max_elm
            i+=1

        return arr
                        

            
                
            



        








        