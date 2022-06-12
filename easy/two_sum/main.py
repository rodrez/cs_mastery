from typing import List

def naive_two_sum(nums: List[int], target: int) -> List[int]:
    """
        How does it work?

        Since this is a naive solution, we can use nested loops.

        The first loop simple iterates over the array as usual.
        Now the second one is a little bit more tricky.
        The second loop will loop through the remainder of the the array after 
        the first loop.

        For example:

        Given an array such as nums = [1,2,3,4]

        The first loop will start at index 0 in this case grabbing "1".
        Now the second loop starts after index 0.

        So it would look something like this:

        
        # nums in first loop is [1, 2, 3, 4]
        for num in nums:
            # nums in nested loop is [2, 3, 4]
            for n in nums[i+1:]:
                pass
    
        Now that we understand the logic behind the nested loop we
        can start comparing the values until we find the two numbers
        that match the target.

        To do this we need to simply grab the value from the parent loop and 
        the nested one.

        for num in range(len(nums)):
            # nums in nested loop is [2, 3, 4]
            for n in range(len(nums[i+1:])):
                if nums[num] + nums[num+n+1] == target:
                    return [num, num+n+1]


    """
    for num in range(len(nums)):
        for n in range(len(nums[num + 1:])):
            if nums[num] + nums[n + num + 1] == target:
                return [num, n + num + 1]


def hash_two_sum(nums: List[int], target: int) -> List[int]:
    """
    How does it work?

    Enter hash map!

    Out of the box thinking at it's best. 
    If this solution never crossed your mind before, 
    don't worry you are not alone.

    Alright enough chit chat...

    We will complete this one with only one for loop.

    First we need t create a variable to hold our dict... I mean our hash map...

    After we have our hashmap ready we start our loop. Our loop must have index, because we will 
    be using the values in the array as keys and the index as our values for our hash map.

    The trick is perform by subtracting the current element from the target. 
    Then adding the element to the hashmap.
    And finally trying to check if the remainder of our subtracting is a key in our hashmap.

    I know it's a bit confusing, but we'll go over it now.
    
    """
    hash_map = {}

    for i, num in enumerate(nums):
        remainder = target - num
        if hash_map.get(remainder) != None:
            return hash_map.get(remainder), i
        hash_map[num] = i
    

    # Explain enumerate

assert hash_two_sum([2,7,11,15], 9) == (0,1), "Should be [0,1]"
assert hash_two_sum([3,2,4], 6) == (1,2), "Should be [1,2]"
assert hash_two_sum([3,3], 6) == (0,1), "Should be [0,1]"
print("Naive test have been completed.")
    
