class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        



if __name__=="__main__":
    

    s = "khar rahkt"

    left_counter=0
    right_counter=len(s)-1

    isPalidrome=True



    while left_counter<right_counter:
        if s[left_counter] == " ":
            left_counter+=1
        
        elif s[right_counter] == " ":
            right_counter-=1

        elif s[left_counter] == s[right_counter]:
            isPalidrome=True
            right_counter-=1
            left_counter+=1

        else:
            isPalidrome=False
            break



    
    print(isPalidrome)