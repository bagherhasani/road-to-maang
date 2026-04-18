class Solution(object):
    def jump(self, nums):
        jumps=0
        current_end=0
        max_reach=0

        for i in range(len(nums)-1):
            max_reach=max(max_reach,i+nums[i])

            if i==current_end:
                jumps+=1
                current_end=max_reach

        return jumps
        
        # scan through the array and every time you reach the end of your current jump's range, 
        # you're forced to jump again — count that.



if __name__=="__main__":
    print("hi")

    nums=[2,3,1,1,4]
    max_reach=0
    jumps=0
    current_end=0


    for i in range(len(nums)-1):
        max_reach=max(max_reach,i+nums[i])

        if i==current_end:
            jumps+=1
            current_end=max_reach

    print(jumps) 
