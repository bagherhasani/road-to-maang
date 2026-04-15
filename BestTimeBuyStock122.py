


import profile


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        

if __name__=="__main__":
    prices = [1,2,3,4,5]
    prices= [7,1,5,3,6,4]
    prices= [1,5]

    buy=prices[0]
    max_profit=0

    for i in range((len(prices)-1)):
        
        # if prices[i]<buy:
        #     buy=prices[i]

        if prices[i+1]>prices[i]:
            max_profit+=prices[i+1]-prices[i]


    print(max_profit)

