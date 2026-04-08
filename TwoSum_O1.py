


if __name__ =="__main__":
    print("hell no")


numbers=[5,6,2,1]
target=3

seen={}

for i in range(len(numbers)):
    complement=target-numbers[i]
    if complement in seen:
        print([seen[complement], i])

    else:
        seen[numbers[i]]=i
