if __name__=="__main__":
    """
    - this tutorial is for the modulo= remainding after division
    - Also called wrapper





    """

  #clock Example 

    print(11+3)  # it is 11 add 3 hours
    print(14%12) # clock is 2 


 # array examples: array has 5 slots(0,1,2,3,4,5) you are in slot 4 move 2 step forward
    print(4+2)
    print(6%5) # we land on slot 1

 # the usage: whenever you need to stay within a fixed range and wrap use %size
    print(8%3)
    print(7%7)
    print(10%4)



 #playlist reapet
    songs = ["A", "B", "C", "D", "E"]
    current = 4
    skip = 3

    print(songs[(current+skip)%len(songs)]) # 3 foward from E is C



  #workers:you have 3 workers. you distribute tasks one by one. 
         # when you run out of workers you start over from worker 0.
    
    tasks = [0, 1, 2, 3, 4, 5]
    workers = 3  

    for i in range(len(tasks)):
        print(f"task {tasks[i]} → worker {tasks[i] % workers}")


    # weekdays
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    today = 0  # Friday
    add = 14

    print(days[(today+add)%len(days)])
