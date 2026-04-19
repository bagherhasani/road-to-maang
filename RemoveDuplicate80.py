

class Solution(object):
    def removeDuplicates(self, nums):
        left=0
        leftmost=0

        while left < len(nums):
            if leftmost < 2:
                nums[leftmost] = nums[left]
                print(f"nums[leftmost] = nums[left]:{nums[leftmost] , nums[left]}")
                left += 1
                leftmost += 1
                print(f"left:{left}     leftmost:{leftmost}")
            elif nums[leftmost-2] == nums[left]:
                print(f"leftmost-2:{leftmost-2}")
                left += 1
            else:
                print(f"left:{left}     leftmost:{leftmost}")
                nums[leftmost] = nums[left]
                left += 1
                leftmost += 1
                

        return leftmost
                
       
class SolutionBaq(object):
    def removeDuplicate(self,nums):
        left=0
        leftmost=0

        while left<len(nums):

            if leftmost<2:
                nums[leftmost]=nums[left]
                left+=1
                leftmost+=1

            elif nums[leftmost-2]==nums[left]:
                #do nothing and skip 
                left+=1

            else:
                nums[leftmost]=nums[left]
                left+=1
                leftmost+=1
            
        return leftmost

        
    


if __name__=="__main__":
    print("hi")
    sol=Solution()

    solbaq=SolutionBaq()


    nums = [1,2,1,2,1,2]

    
    print(sol.removeDuplicates(nums))

    print(solbaq.removeDuplicate(nums))
    
    



    
