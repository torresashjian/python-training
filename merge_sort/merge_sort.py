# MergeSort Class
class MergeSort:
    
    def merge_sort(self, arr):
        arrLen = len(arr)
        if arrLen > 1:
            left = self.merge_sort(arr[:arrLen/2])
            right = self.merge_sort(arr[arrLen/2:])
            return self.merge(left, right)
        else:
            return arr
            
    def merge(self, l, r):
        totalLen = len(l) + len(r)
        lInd = 0
        rInd = 0
        count = 0
        sorted_arr = []
        while count < totalLen:
            if lInd == len(l):
                sorted_arr.append(r[rInd])
                rInd = rInd + 1
            elif rInd == len(r):
                sorted_arr.append(l[lInd])
                lInd = lInd + 1
            elif l[lInd] < r[rInd]:
                sorted_arr.append(l[lInd])
                lInd = lInd + 1
            else:
                sorted_arr.append(r[rInd])
                rInd = rInd + 1
            count = count + 1
            
        return sorted_arr
        