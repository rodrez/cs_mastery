
import string
def isPalindrome( s: str):


    whitelist = set(string.ascii_lowercase + string.digits )
    word = ''.join(filter(whitelist.__contains__, s.lower()))


    left, right = 0, -1
    while left < len(word)/2:
        print(left)
        if word[left] != word[right]:
            return False
        left += 1
        right -= 1
    return True






print(isPalindrome(""))