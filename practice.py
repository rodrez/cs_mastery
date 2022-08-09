from typing import List

def topKFrequent(nums: List[int], k: int) -> List[int]:

    hash1 = {}

    for num in nums:
        hash1[num] = hash1.get(num, 0) + 1

    results = {num: [] for num in range(len(nums)+1) }

    for key, value in hash1.items():
        results[value].append(key)

    end = [] * k
    for i in range(len(results.values()) -1, -1, -1):
        print(results.values())
        for j in results.values()[0][i]:
            print(j)
            if end < k:
                end.append(j)




topKFrequent(nums = [1,1,1,2,2,3,4,4,4], k = 2)



# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# Input: nums = [1], k = 1
# Output: [1]