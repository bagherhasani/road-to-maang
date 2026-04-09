class Solution(object):

    # the solution is we use a copy of the array to go over
    # but  we remove the item from original array
    # ! we cannot go over orignal and remove item because as we delete items the iteration will be wrong 
    


    def removeElement(self, nums, val):
        
        for i in range(len(nums)):
           if nums[i]==val:
               nums.remove(nums[i])
               print(f"i:{i}, value:{nums[i]}")

        return len(nums)
        
       

        
        







if __name__=="__main__":
    print("main")

    nums=[0,1,2,2,3,0,4,2]
    val=2

    sol=Solution()
    sol.removeElement(nums,val)