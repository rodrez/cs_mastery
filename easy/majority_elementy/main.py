from typing import List


def majorityElement(nums: List[int]) -> int:
    mapper = {}


    for num in nums:
        mapper[num] = mapper.get(num, 0) + 1
        if mapper[num] >= len(nums) / 2:
            return num


    return max(mapper.items())

print(majorityElement([3,4,3,4]))