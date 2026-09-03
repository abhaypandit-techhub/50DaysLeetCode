class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
           return False
        num=x
        sum=0
        while(num>0):
            rem=num%10
            num=num//10
            sum=sum*10+rem
        if sum == x :
            return True
        else :
            return False       
        