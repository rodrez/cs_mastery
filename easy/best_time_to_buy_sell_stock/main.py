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

def ptrMaxProfit(prices: List[int]) -> int:
    # Create max_profit, left ptr, right ptr var
    # Assing index 0 to the left pointer and index 1 to the right pointer
    # Loop through the array and subtract the right pointer from the left in each iteration
    # if the result is greater than max_profit then update max_profit, else move the right pointer
    # If the right pointer is
    # Create a max var to hold the highest amount if negative return 0
    max_profit = 0
    l, r = 0,1
    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            max_profit = max(max_profit, profit)
        else:
            l = r 
        r += 1
    return max_profit

def sorted_group_anagram(array):
    hashmap = {}
    for word in array:
        sorted_word = tuple(sorted(word))

        hashmap[sorted_word] = hashmap.get(sorted_word, []) + [word]

    return hashmap.values()
# print(ptrMaxProfit([]))
s = sorted_group_anagram(["eat","ate","bat"])
print(s)