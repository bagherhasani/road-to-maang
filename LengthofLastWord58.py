from operator import contains


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        

if __name__=="__main__":
    s= "a   "
    length=0
    for i in range(len(s)-1,-1,-1):
        if s[i]==" " and s[i-1]==" ":
            print(i)
        elif s[i]!=" ":
            length+=1
            if s[i-1]==" ":
                break
            

    print(length)