def singleNumber(nums):

    hashm = {}
    for num in nums:
        hashm[num] = hashm.get(num, 0) + 1

    for k, v in hashm.items():
        if v == 1:
            return k

# print(singleNumber([2,1,1]))

def singleNumber3(nums):
    print(set(nums))
    print(sum(set(nums)))
    print(sum(nums))
    return 2*sum(set(nums))-sum(nums)


print(singleNumber3([2,1,1]))