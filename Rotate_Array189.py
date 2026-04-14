class Solution(object):
    def rotate(self, nums, k):
        newnums=[0]*len(nums)

        for i in range(len(nums)):
            newnums[(i+k)%len(nums)]=nums[i]

        nums[:]=newnums

        return nums
         
    


if __name__=="__main__":
    print("hi")

    sol=Solution()

    nums=[1,2,3,4,5,6,7]
    nums1=[1,2,3,4,5,6,7]

    k=1

    newnums=[0]*len(nums)

    for i in range(len(nums)):
        print((i+k)%len(nums))
        newnums[(i+k)%len(nums)]=nums[i]

    nums[:]=newnums


    print(nums)

    print(sol.rotate(nums1,k))