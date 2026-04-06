

students={} # creating a hash table 

students["name"]="Baqer"
students["age"]=25
students["grade"]="A"

# read from it 
print(students["name"])

# check if the key exists
print("age" in students)

#deleting a key
del students["age"]


print(students)


print(hash("Alice"))


# Solving A problem with Hash tables ----> Find if any number appears more than once.
#-----------------------------------------------------------------------------


numbers = [3, 7, 2, 9, 3, 5,3,3,3,5]

seen={}

for item in numbers:
    if item in seen:
        print(item, "is a duplicate")
    else:
        seen[item]=True


