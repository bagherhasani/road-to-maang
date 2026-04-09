from unittest import result


class Solution(object):
    def merge(self, nums1, m, nums2, n):
       
       #whatever after index m be nums2 we merge nums2 into nums1 empty spot and then we sort 
        nums1[m:]=nums2
        nums1.sort()
        


if __name__== "__main__":

    nums1=[1,4,3,4]
    nums2=[5,6,7]

    print(nums1[:3])
 

    sol=Solution()
    result=sol.merge(nums1,4,nums2,3)

    print(nums1)

    nums1=nums1[2:]
    print(nums1)

