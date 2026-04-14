from math import floor


class Solution(object):
    def majorityElement(self, nums):
        n= len(nums)/2
        seen={}

        for i in range(len(nums)):
            if nums[i] in seen:
                seen[nums[i]]+=1
                if seen[nums[i]]>floor(n): 
                    return nums[i]
            else:
                seen[nums[i]]=1

        return max(seen, key=seen.get)
    




class SolutionBaq(object):

    def findMajorityElement(self,nums):
       seen={}

       for i in range(len(nums)):
           if nums[i] in seen:
               seen[nums[i]]+=1
               if seen[nums[i]]>floor(len(nums)/2):
                   return nums[i]

           else:
               seen[nums[i]]=1
           

       return max(seen,key=seen.get)


if __name__=="__main__":
    print("hey")
    sol = Solution()
    solbaq=SolutionBaq()


    nums=[1,2,2]
    print(sol.majorityElement(nums))

    print(solbaq.findMajorityElement(nums))



    # seen={}
    # treshhold = floor(len(nums)/2)

    # for item in nums:
    #      if item in seen:
    #           seen[item]+=1
    #           if seen[item]>treshhold:
    #               print(item)

    #      else:
    #          seen[item]=1
    # print(seen)
  