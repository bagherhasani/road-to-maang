from operator import le


class Solution(object):
    def mergeAlternately(self, word1, word2):
        i=0
        j=0
        merged=""
        while (len(word1)>i or len(word2)>j):

            merged+=word1[i]
            merged+=word2[j]

            print(word1[i])
            print(word2[j])
            i+=1
            j+=1
        return merged
    


if __name__=="__main__":
    word1 = "ab"
    word2 = "pqrs"
    Output= word1+word2

    #print(len(Output))

    i=0
    j=0
    merged=""
    while (len(word1)>i or len(word2)>j):

        if i<len(word1):
            merged+=word1[i]

        if j<len(word2):
            merged+=word2[j]
        
        i+=1
        j+=1
       
    print(merged)

       
   