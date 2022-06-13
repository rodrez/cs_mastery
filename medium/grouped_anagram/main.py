from collections import defaultdict
from typing import List

def sorted_group_anagram(self, strs: List[str]) -> List[List[str]]:
    # Loop through the array
    # sort the word
    # use the sorted word as key in hash map, don't forget to make it a tuple
    # Add word to the key
    hashmap = {}
    for word in strs:
        sorted_word = tuple(sorted(word))

        hashmap[sorted_word] = hashmap.get(sorted_word, []) + [word] 
    
    return hashmap.values()


def hash_group_anagram(array):
# Input: strs = 
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Loop trough array 
# Loop through words
# Match the position of each letter to an index of an array
# Increase the count 
# Use the array with the counts as the key for the default dict and append the words to that key 
#  
    hashmap = defaultdict(list)
    for word in array:
        temp = [0] * 26
        for letter in word:
            temp[ord(letter) - ord('a')] = temp[ord(letter) - 97] + 1
        
        hashmap[tuple(temp)].append(word)

    print(hashmap.values())



