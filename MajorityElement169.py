from math import floor


class Solution(object):
    def majorityElement(self, nums):
        
        return 0 
    



if __name__=="__main__":
    print("hey")


    nums=[2,2,1,1,1,2,2]
    seen={}
    n=len(nums)/2

    for i in range(len(nums)):
        if nums[i] in seen:
            seen[nums[i]]+=1
            if seen[nums[i]]>floor(n):
                print(nums[i])


        else:
            seen[nums[i]]=1
  