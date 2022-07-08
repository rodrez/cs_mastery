from typing import List

def topKFrequent(nums: List[int], k: int) -> List[int]:

    # Holds the counts in a dictionary
	counts = {}

    # Create a list of list based on the nums length
	frequency = [[] for i in range(len(nums)+1)]
	
    # Loop through the nums list
	for num in nums:
        # If the num is in the dictionary, increment the count
        # As usual we use the get method to return the value if it exists
        # And if it doesn't exist, we pass in the default value of 0 and add one to it
        # This avoids the need to check if the key exists
		counts[num] = counts.get(num ,0) + 1
	
    # Loop through the dictionary
	for value, count in counts.items():
        # Add the value to the list at the index of the count
		frequency[count].append(value)
	
    # Holds the end result
	result = []

    # Loop through the frequency list starting from the end
	for i in range(len(frequency), 1,-1):
		
        # Loop through the list at the index of i
		for n in frequency[i-1]:
            # Add the value to the result list
			result.append(n)

            #  If the length of the result list is equal to k, return the result
			if len(result) == k:
				return result
	return result