def solution(sequence):
    droppped = False
    last = prev = min(sequence) - 1
    for elm in sequence:
        if elm <= last:
            if droppped:
                return False
            else:
                droppped = True
            if elm <= prev:
                prev = last
            elif elm >= prev:
                prev = last = elm
        else:
            prev, last = last, elm
    return True


def solution(sequence):

    removed = 0
    i = 0
    prev = min(sequence) - 1

    while removed < 2 and i < len(sequence):

        # Checks if the current index is greater than the previous one
        if sequence[i] > prev:
            prev = sequence[i]

        #
        elif i == len(sequence) - 1 or sequence[i + 1] > sequence[i - 1]:

            removed += 1

        elif i < 2 or sequence[i] > sequence[i - 2]:

            removed += 1
            prev = sequence[i]
        else:
            return False

        i += 1

    return removed < 2


s = solution([1, 3, 2, 1])
s2 = solution([1, 3, 2])
s3 = solution([1, 2, 1, 2])
s4 = solution([10, 1, 2, 3, 4, 5])
s5 = solution([1, 2, 3, 4, 5, 3, 5, 6])
s6 = solution([1, 1])
s7 = solution([40, 50, 60, 10, 20, 30])
# s8 = solution([0, -2, 5, 6])
# s9 = solution([1, 2, 3, 4, 99, 5, 6])
# s10 = solution([1])


print("S (False): ", s)
print("S2 (True): ", s2)
print("S3 (False): ", s3)
print("S4 (True): ", s4)
print("S5 (False): ", s5)
print("S6 (True): ", s6)
print("S7 (False): ", s7)
# print("S8 (True): ", s8)
# print("S9 (True): ", s9)
# print("S10 (True): ", s10)
