


class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        start_position=-100
        tank=0

        for i in range(len(gas)):
            if gas[i]-cost[i]>=0:
                start_position=i


        for i in range(len(gas)):
            start_station=(start_position+i) % len(gas)
            tank+=gas[start_station]-cost[start_station]
            print(tank)
            if tank<0:
                return -1

            if i == len(gas)-1:
                return start_position
            
        return -1





if __name__=="__main__":
    gas=[5,1,2,3,4]
    cost=[4,4,1,5,1]
    start_position=-1
    max_pos=0
    tank=0

    for i in range(len(gas)):
        if gas[i]-cost[i]>=0 and gas[i]-cost[i]>max_pos:
            max_pos=i
            start_position=i
            


    for i in range(len(gas)):
        start_station=(start_position+i) % len(gas)
        tank+=gas[start_station]-cost[start_station]
        print(tank)
        if tank<0:
            print("Failed")
            break

        if i == len(gas)-1:
            print("Reached")
            break


    sol=Solution()
    print("Final Solution")
    print(sol.canCompleteCircuit(gas,cost))