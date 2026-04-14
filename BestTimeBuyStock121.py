
if __name__=="__main__":

    prices = [7,1,5,3,6,4]
    prices = [2,4,1]

    buy=prices[0]
    max_profit=0

    for i in range(1,len(prices)):
        if prices[i]<buy:
            buy=prices[i]
        
        profit=prices[i]-buy
        if profit>max_profit:
            max_profit=profit


    print(max_profit)
    
    