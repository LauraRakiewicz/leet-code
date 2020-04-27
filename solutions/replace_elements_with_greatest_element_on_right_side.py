class Solution(object):
    def replaceElements(self, arr):
        out = []
        for i in range(0,len(arr)-1):
            max_right = max(arr[i+1:])
            print(max_right)
            out.append(max_right)
        out.append(-1)
        return out 
        