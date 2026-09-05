class Solution(object):
    def findLucky(self, arr):
        dict={}
        lst=[]
        for i in arr:
            dict[i]=dict.get(i,0) + 1
        for j in range(1,len(arr)+1) :
            if j==dict.get(j,-1):
                lst.append(j)      
        return max(lst) if lst else -1             



        