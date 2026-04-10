


class Solution(object):
    def removeDuplicates(self, nums):

        # nested not working for this problem as we remove the item it gets messy
        for i in nums[:]:
            for j in nums[i+1:]:
                if i==j:
                    print(f"i:{i}   j:{j}")
                    nums.remove(i)
                    print(f"nums:{nums}")



    # working with the hashmap 
    def removeDuplicates2(self, nums):
        seen={}

        for item in nums:
            if item not in seen:
                seen[item]=1

      
        nums[:]=seen.keys()
        print(seen)
        return len(seen)


    


    


if __name__=="__main__":
   print("he")

nums=[1,2,1,2]

sol=Solution()

print(sol.removeDuplicates2(nums))



   