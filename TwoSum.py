from operator import le


class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    return i,j
                


if __name__ =="__main__":
    sol=Solution()
    nums=[5,6,2,1]
    target= 3


    # result=sol.twoSum(nums,target)

    # print(f"Indices:{result}")


for i in range(len(nums)):
   for j in range(i+1,len(nums)):
       print(f"i:{nums[i]}  j:{nums[j]}")
       if nums[i]+nums[j]==target:
           print(f"Result : i:{i}={nums[i]}    j:{j}={nums[j]}")



phonebook = {}

phonebook["ali"]="918"
phonebook["reza"]="912"

print(phonebook)

# looking up
print(phonebook["ali"])

if "sara" in phonebook:
    print("found sara",phonebook["sara"])

if "bob" in phonebook:
    print("bob sara",phonebook["bob"])
else:
    print("bob not found")


numbers=[1,2,3,4]
seen={}

for i in range(len(numbers)):
    seen[numbers[i]]=i
    print(f"i={i}, val={numbers[i]}, seen={seen}")

print(2 in seen)
print(seen[2])


    




