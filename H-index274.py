class Solution(object):
    def hIndex(self, citations):
         def hIndex(self, citations):
            citations.sort(reverse=True)
            h = 0
            counter=0

            for i in range(len(citations)):
                    counter+=1
                    if citations[i]>=counter:
                        h=counter

            return h
             


    def hIndexR(self,citatiosn):
         h=0
         counter=0
         citations.sort(reverse=True)

         for i in range(len(citations)):
              counter+=1
              if citations[i]>=counter:
                   h=counter
         return h


if __name__=="__main__":

    citations=[3, 0, 6, 1, 5]
    citations=[1,3,1]

    citations.sort(reverse=True)
    h=0

    counter=0

    for i in range(len(citations)):
            counter+=1
            if citations[i]>=counter:
                h=counter

    print(h)

