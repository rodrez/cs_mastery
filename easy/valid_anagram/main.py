

def hash_is_anagram(first_word: str, second_word: str) -> bool:
    """
    What is an anagram?

    An anagram is a word or phrase that can be formed by using the
    exact same letters from another word.
    
    An example of an anagram is the word HEART, and EARTH.
    We use the exact same letters to form a completely different word.

    Alright, how do we tackle this one?

    The easiest solution that comes to mind is to count all letter occurrences
    and storing them in a hashmap or python's evil twin `dict`.

    To make this work we will have to loop through both words, 
    save the letter as the key and keep adding to that letter count 
    if a new occurrence is found to the value.

    Our dict would look like this for the word HEART:

    anagram_hash_map = {
        "H":1,
        "E":1,
        "A":1,
        "R":1,
        "T":1
    }

    In this example we do not have any duplicate letter,
    but if we did then we would simply add it to its respective key.

    For example the HELLO word would yield the following:
    anagram_hash_map = {
        "H":1,
        "E":1,
        "L":2,
        "O":1
    }
    Notice how L value is 2 instead of 1, since there where two occurrences 
    for the letter O.

    Time Complexity: O(n) -> Two for loops n letters in the word
    Space Complexity: O(n) -> Two variables created for the hashmap

    """

    first_hash_map = dict()
    second_hash_map = dict()

    # Loops through the first word and creates a hashmap
    # with a count of each letter occurrence
    for letter in first_word:
        # We used `.get()` to avoid Key Error:
        first_hash_map[letter] = first_hash_map.get(letter, 0) + 1
        
    for _letter in second_word:
        second_hash_map[_letter] = second_hash_map.get(_letter, 0) +1

    # Compares both hash_maps
    return first_hash_map == second_hash_map


def sort_is_anagram(s: str, t: str) -> bool:
    """
    How does this solution works?

    The basis of this solution is to sort both strings
    and then compared them.

    Why does this works?

    It works because when we sort the word HEART, we get the following:

    Note: In python a quick way to sort a word in python is to use the `sorted(your_word)` function.
    Do remember that majority of sorts have a time complexity of O(n log n) 
    
    `['A', 'E', 'H', 'R', 'T']`
    
    Now, for the other word to be an anagram of HEART what do you think we should get? 
    Yes! You are correct, we should get the exact same sorted array as above 
    for it to be an anagram. 

    Let's try it...
    
    `['A', 'E', 'H', 'R', 'T']`

    Would you look at that!?

    We have already done most of the work. At this point we simply compare the two arrays for equality.
    If the arrays are equal, then we return True.
    Otherwise, we return False since the we do not have an anagram.

    Time Complexity: O(n log n) -> Due to sorting
    Space Complexity: O(1) -> No variables created for the hashmap

    """
    return sorted(s) == sorted(t)



assert hash_is_anagram("FRIED", "FIRED") == True, "Should be True"
assert hash_is_anagram("EARTH", "HEART") == True, "Should be True"
assert hash_is_anagram("HAM", "JAM") == False, "Should be False"
assert hash_is_anagram("anagram", "nagaram") == True, "Should be False"
assert hash_is_anagram("rat", "car") == False, "Should be False"
print("All Hash Solution test passed.")

assert sort_is_anagram("FRIED", "FIRED") == True, "Should be True"
assert sort_is_anagram("EARTH", "HEART") == True, "Should be True"
assert sort_is_anagram("HAM", "JAM") == False, "Should be False"
print("All Sort Solution test passed.")