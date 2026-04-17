import logging


logging.basicConfig(level=logging.DEBUG, format='%(message)s')
log = logging.getLogger()




class Solution(object):
    def canJump(self, nums):
        max_reach=0
        if len(nums) == 1:
                return True

        for i in range(len(nums)):
            step_reach=i+nums[i]


            if step_reach>max_reach:
                max_reach=step_reach

            
            if i >= max_reach and nums[i]==0 :
                return False
            
            if max_reach>=len(nums)-1:
                return True
            

        return False
        


        
        



if __name__=="__main__":
    print("hi")

    nums = [1,0,1]
    # nums=[0]

    max_reach=0
    result = False

    if len(nums)==1:
         print("True")

    for i in range(len(nums)):
         cur_reach=i+nums[i]

         if cur_reach>max_reach:
              max_reach=cur_reach

         log.debug(f"i={i} val={nums[i]} cur_reach={cur_reach} max_reach={max_reach}")

         if i >= max_reach and nums[i]==0:
              log.debug("STUCK - False")
              result = False
              break

         if max_reach >= len(nums)-1:
              log.debug("REACHED END - True")
              result = True
              break
    
    log.debug(f"final result: {result}")
    
    
    
    
    
    
    nums2 = [1,0,1]
    
    sol =Solution()

    print(sol.canJump(nums2))