class Solution(object):
    def isThree(self, n):
        import math

        num=n
        lst=[]
        for i in range(1,int(math.sqrt(num))+1):
            if num%i==0: 
                lst.append(i)
                if i != num//i:
                    lst.append(n//i)
        sum=len(lst)            
        if sum == 3 :
            return True
        else :
            return False     


        