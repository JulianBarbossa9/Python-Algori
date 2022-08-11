
'''
max_profit = 0
for price in range 5
   for j in range (price + 1, 6)
    profit =  - 
'''



def maxProfit(prices):
    max_profit = 0
    for price in range(len(prices) - 1):
        for j in range(price + 1, len(prices)):
            profit = prices[j] - prices[price]
            if profit > max_profit:
                max_profit = profit
    return max_profit
    
    

listp = [7, 1, 5, 3, 6, 4]
prueba = maxProfit(listp)
print(prueba)
