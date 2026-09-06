class Solution(object):
    def firstUniqChar(self, s):
        hash_list=[0]*27
        for ch in s:
            index=ord(ch)-97
            hash_list[index]+=1
        for ch in s:
            index=ord(ch)-97
            if hash_list[index]==1:
                return s.index(ch)
        return -1    


      
        