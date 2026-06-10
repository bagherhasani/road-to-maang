from fractions import gcd

class Solution(object):
    def gcdOfStrings(self, str1, str2):
        if str1+str2!=str2+str1:
            return ""
        gcds=gcd(len(str1),len(str2))
        return str1[:gcds]
        



if __name__=="__main__":
    """
 Example 1:
    Input: str1 = "ABCABC", str2 = "ABC"
    Output: "ABC"

Example 2:
    Input: str1 = "ABABAB", str2 = "ABAB"=
    Output: "AB"

Example 3:
    Input: str1 = "LEET", str2 = "CODE"
    Output: ""

Example 4:
    Input: str1 = "AAAAAB", str2 = "AAA"
    Output: ""

    """


str1="ABCABC"
str2="ABC"

str1 = "ABABAB"
str2 = "ABAB"


# str1 = "AAAAAB"
# str2 = "AAA"


str1 = "TAUXXTAUXXTAUXXTAUXXTAUXX"
str2 = "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"

i = len(str1)-1
j= len(str2)-1



counter=0
gcd=math.gcd(len(str1),len(str2))
result=""

while(counter!=gcd):
    
    if str1[i]== str2[j]:
        result+=str2[j]
    else:
        result=""
        break

    i-=1
    j-=1
    counter+=1




print(result[::-1])



str11="ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZQJXZKMPVYWTBAOHNRLIEGDSCUFABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
str12="ABCDEFGHIJKLMNOPQRSTUVWXYZZYXWVUTSRQPONMLKJIHGFEDCBAABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(len(str11))
print(len(str12))
print(math.gcd(130,78))
print(78/26)