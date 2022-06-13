from typing import List

def naiveMaxProfit(prices: List[int]) -> int:
    # Loop through the array
    # Collect the first item and then loop through the reminder of the array
    # Create a max var to hold the highest amount if negative return 0
    max_profit = 0
    for i in range(len(prices)):
        for j in prices[i+1:]:
            if j - prices[i] > max_profit:
                max_profit = j - i
    return max_profit

def naiveMaxProfit(prices: List[int]) -> int:
    # Loop through the array
    # Collect the first item and then loop through the reminder of the array
    # Create a max var to hold the highest amount if negative return 0
    max_profit = 0
    for i in range(len(prices)):
        pass
    return max_profit


print(maxProfit([7,6,4,3,1]))