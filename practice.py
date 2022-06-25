def my_sqrt(x: int) -> int:
    r = x
    while r*r > x:

        r = (r + x/r) // 2
        print("Step 2: ", r)
    return int(r)

def binary_my_sqrt(x):
    left, right = 0, x

    while left <= right:
        print("Left: ", left)
        print("Right: ", right)


        mid = (left + right) // 2
        print("Mid: ", mid)
        if mid * mid > x:
            right = mid - 1
        elif mid * mid < x:
            left = mid + 1
        else:
            return mid

    # When there is no perfect square, hi is the the value on the left
    # of where it would have been (rounding down). If we were rounding up,
    # we would return lo
    return left

print(binary_my_sqrt(99))