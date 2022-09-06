from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    hashmap = {}

    for i, val in enumerate(nums):
        print(hashmap)
        print(target - val)
        if target - val in hashmap.keys():
            return i, hashmap[target - val]
        hashmap[val] = i

print("Results: ",twoSum([3,2,4], 6))