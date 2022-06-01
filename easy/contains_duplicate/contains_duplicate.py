import sys
import os
sys.path.append(os.path.join(sys.path[0], '../..'))

from typing import List

from utils.helper import timeit, large_array


@timeit
def naive_solution(nums: List[int]) -> bool:
    """
        How does it work?
        Given array [1,2,3,1]
        The first loop selects the first element in this case `1`.
        
        Next, the second loops starts after the first element selected
        in the first loop. In this case `2`

        Then the conditional if statement compares the to numbers for equality.
        If the numbers are equal True is returned, otherwise we repeat step 1 at the next element.

        Time Complexity: O(n²) (Because of nested for loops)
        Space Complexity: O(1) (No new variable assigned)

    """
    # Loops trough the list 
    for i in nums:
        # Loops through the list but starts at the 
        for j in nums[i:]:
            if i == j:
                return True
    return False

@timeit
def sorted_solution(nums: List[int]) -> bool:
    """
        How does it work?
        Given array [1,2,3,1]

        The first thing we do is sort the list.
        Some programming languages, have array methods to perform 
        sorting. 

        After we sort the array/list, we need to check all elements
        using a loop and verifying the adjacent element.

        Example:
        
        After the array is sorted it would become: [1,1,2,3]
        Next, the for loop would go through the first element, 
        Additionally, we need a conditional if statement to compare 
        the current element and the adjacent element to the left.
        
        If the elements are the same, then we return True,
        otherwise we continue the loop. 

        If no elements are found to be duplicate we return False after the 
        loop is done.

        Time Complexity: O(n log(n)) (Because of sorting)
        Space Complexity: O(n) (New variable assigned)

        Note: O(n log(n)) is slightly better than O²
    """ 

    sorted_array = sorted(nums)
    for n in range(len(sorted_array)):
        if n < len(sorted_array)-1 and sorted_array[n] == sorted_array[n+1]:
            return True
    return False

@timeit
def set_solution(nums:List[int]) -> bool:
    """
        How does it work?
        Given array [1,2,3,1]

        First, we will create a new set variable.
        Then, we loop through the array
        If the item is not in set, we added, otherwise,
        the item is already in the set, so we can return True.

        If none of the items is duplicate we return false after the loop.
    """

    hash_set = set()
    for n in nums:
        if n in hash_set: 
            return True
        # Else can be ignored but it's added for explicitness (easier to read imo)
        else:
            hash_set.add(n)
    return False


def clever_solution(nums: List[int]) -> bool:
    """
        How does it work?
        Given array [1,2,3,1]

        In the case of Python we can verify for duplicates by leveraging `set()`

        `set()` build a collection of unordered unique elements. 

        Taking that in consideration we can simply compare the length of the original array,
        versus the length of the array that we converted to a set.

        Because `set()` drops duplicates if the arrays are not the same length that means,
        there were duplicates.


    """
    return len(set(nums)) != len(nums)




# Naive Test
# assert naive_solution([1,2,3,1]) == True, "Should be True"
# assert naive_solution([1,2,3,4]) == False, "Should be False"
# assert naive_solution([1,1,1,3,3,4,3,2,4,2]) == True, "Should be True"
# print("All naive test passed!")

# Sorted Test
# assert sorted_solution([1,2,3,1]) == True, "Should be True"
# assert sorted_solution([1,2,3,4]) == False, "Should be False"
# assert sorted_solution([1,1,1,3,3,4,3,2,4,2]) == True, "Should be True"
# print("All sorted test passed!")

# Hash Set Test
# assert set_solution([1,2,3,1]) == True, "Should be True"
# assert set_solution([1,2,3,4]) == False, "Should be False"
# assert set_solution([1,1,1,3,3,4,3,2,4,2]) == True, "Should be True"
# print("All hash tests passed!")

# Hash Set Test
assert clever_solution([1,2,3,1]) == True, "Should be True"
assert clever_solution([1,2,3,4]) == False, "Should be False"
assert clever_solution([1,1,1,3,3,4,3,2,4,2]) == True, "Should be True"
print("All hash tests passed!")