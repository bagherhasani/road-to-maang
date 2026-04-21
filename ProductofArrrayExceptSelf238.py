from math import prod

class Solution(object):
    def productExceptSelfBaq(self, nums):
        result=[0]*len(nums)
        for i in range(len(nums)):
            result[i]=prod(nums[:i])*prod(nums[1+i:])


        return result
        

    def productExceptSelf(self,nums):
        res=[1]*len(nums)

        prefix=1
        postfix=1

        for i in range(len(nums)):
            res[i]=prefix
            prefix*=nums[i]
        
        for i in range(len(nums)-1,-1,-1):
            res[i]*=postfix
            postfix*=nums[i]

        return res



if __name__=="__main__":
    print("HI")

    prefix=[]
    suffix=[]

    nums=[1,2,3,4]
    prefixProductArray=[1]*len(nums)
    suffixProductArray=[1]*len(nums)
    result=[0]*len(nums)

    for i in range(1,len(nums)):
        prefixProductArray[i]=prefixProductArray[i-1]*nums[i-1]
        
    for i in range(len(nums)-2,-1,-1):
        suffixProductArray[i]=suffixProductArray[i+1]*nums[i+1]

    for i in range(len(nums)):
        result[i]=prefixProductArray[i]*suffixProductArray[i]
   



    # print(prefixProductArray)
    # print(suffixProductArray)
    # print(result)




numss=[1,2,3]
result=[1]*len(numss)
prefix=1
postfix=1

for i in range(len(numss)):
    result[i]=prefix
    prefix*=numss[i]
    print(f"prefix:{prefix}")
    print(result)

for i in range(len(numss)-1,-1,-1):
    result[i]*=postfix
    print(f"result[i]:{result[i]}")
    print(f"postfix:{postfix}")
    postfix*=numss[i]
    
    

    