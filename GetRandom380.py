import random




class RandomizedSet(object):

    def __init__(self):
        self.hashmap={}
        self.array=[]
        

    def insert(self, val):
        if val not in self.hashmap:
            self.hashmap[val]=len(self.array)
            self.array.append(val)
            return True
        
        return False
        

    def remove(self, val):
        if val in self.hashmap:
            last_element=self.array[-1]
            index_of_val=self.hashmap[val]

            self.array[index_of_val]=last_element
            self.hashmap[last_element]=index_of_val

            self.array.pop()
            del self.hashmap[val]
            
            return True
        

        return False





        # if val in self.hashmap:
        #     del self.hashmap[val]
        #     self.array.remove(val)
        

    def getRandom(self):
        return random.choice(self.array)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

class RandomizedSetBaq(object):

    def __init__(self):
        self.hashmap={}
        self.array=[]

    def insert(self,val):
        if val not in self.hashmap:
            self.hashmap[val]=len(self.array)
            self.array.append(val)
            return True
        
        return False






    def remove(self, val):
        if val in self.hashmap:
            last_element=self.array[-1]
            index_val=self.hashmap[val]

            self.array[index_val]=last_element
            self.hashmap[last_element]=index_val

            self.array.pop()
            del self.hashmap[val]

            return True
        
        return False




    def getRandom(self):
        return random.choice(self.array)


if __name__=="__main__":
    rs = RandomizedSetBaq()

    print(rs.insert(5))   # True
    print(rs.insert(6))   # True
    print(rs.insert(7))   # True
    print(rs.insert(5))   # False, already exists
    print(f"array: {rs.array}")
    print(f"hashmap: {rs.hashmap}")

    print(rs.remove(5))   # True
    print(f"array: {rs.array}")
    print(f"hashmap: {rs.hashmap}")

    print(rs.getRandom())
    