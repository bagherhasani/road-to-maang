class Solution(object):

    # the solution is we use a copy of the array to go over
    # but  we remove the item from original array
    # ! we cannot go over orignal and remove item because as we delete items the iteration will be wrong 
    

    #for each loop
    def removeElement(self, nums, val):
        for item in nums[:]:
            if item== val:
                nums.remove(item)
        return len(nums)
    

    #We go backward meaning we visit from right to left. 
    # And removals happen on the right side which we already visited. So it doesn't matter if it shifts.

    def removeElement2(self,nums,val):
        for i in range(len(nums)-1, -1, -1):
            if nums[i]==val:
                nums.remove(nums[i])

        return len(nums)

        
       

        
        







if __name__=="__main__":
    print("main")

    nums=[0,1,2,2]
    val=2

    sol=Solution()
    print(sol.removeElement(nums,val))

   
    print(sol.removeElement2(nums,val))