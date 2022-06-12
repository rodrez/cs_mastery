from collections import defaultdict
from typing import List

def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    # Loop through the array
    # sort the word
    # use the sorted word as key in hash map, don't forget to make it a tuple
    # Add word to the key
    hashmap = {}
    for word in strs:
        sorted_word = tuple(sorted(word))

        hashmap[sorted_word] = hashmap.get(sorted_word, []) + [word] 
    
    return hashmap.values()