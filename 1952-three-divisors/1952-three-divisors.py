class Solution(object):
    def isThree(self, n):

        num=n
        sum=0
        for i in range(1,num+1):
            if num%i==0: 
                sum=sum+1
        if sum == 3 :
            return True
        else :
            return False     


        