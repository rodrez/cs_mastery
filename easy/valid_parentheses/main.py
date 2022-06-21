
s = "()[]{}"
s2 = "([]{}"


def isValid(s: str) -> bool:
    """
        First we create a hashmap/dict to hold the opening bracket of a closing one
    """

    closedParent = {
        "{":"}",
        "[":"]",
        "(":")"
    }

    _all = list(s)

    for index, n in enumerate(_all):
        for idx, i in enumerate(_all[index:]):
            if i in closedParent.keys():
                _all.pop(idx)
                _all.pop(index)

# isValid(s)
s = "()[]{}"
s2 = "([]{}"

def isValid2(s: str) -> bool:

    closedParent = {
        "}":"{",
        "]":"[",
        ")":"("
    }

    stack = []

#     Loops trough each parenthesis of the list s
    for c in s:
#         If the  element is in closedParent continue
        if c in closedParent:
#             if the stack has items and the last item equals opening bracket
            if stack and stack[-1] == closedParent[c]:
#                 remove it
                stack.pop()
#           if the stack has items or the last element is not equal to closing bracket
            else:
                return False
#       if the brackt is not in closedParent add it to the stack
        else:
            stack.append(c)
#             if the stack is empty return True otherwise False
    return True if not stack else False

print(isValid2(s2))
