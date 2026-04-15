class Solution(object):
    def maxProfit(self, prices):
        buy=prices[0]
        max_profit=0

        for i in range(len(prices)):
            if prices[i]<buy:
                buy=prices[i]

            profit=prices[i]-buy

            if profit>max_profit:
                max_profit=profit


        return max_profit 


if __name__=="__main__":

    prices = [7,1,5,3,6,4]
    prices = [2,4,1,6]

    buy=prices[0]
    max_profit=0


    soll=Solution()
    print(soll.maxProfit(prices))

    for i in range(1,len(prices)):
        profit=prices[i]-buy

        if prices[i]<buy:
            buy=prices[i]
        
        
        if profit>max_profit:
            max_profit=profit


    print(max_profit)
    
    