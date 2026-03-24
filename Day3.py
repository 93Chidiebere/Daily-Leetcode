# Question: Group words that are anagrams.

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # Initialize a dictionary to store lists of anagrams
        anagram_map = defaultdict(list)
        
        for s in strs:
            # Sort the characters to create a unique key for all anagrams
            # Example: "eat" -> "aet", "tea" -> "aet"
            key = "".join(sorted(s))
            
            # Append the original string to the corresponding group
            anagram_map[key].append(s)
            
        # Return all the grouped lists
        return list(anagram_map.values())


#SQL 

SELECT score, 
       DENSE_RANK() OVER (ORDER BY score DESC) AS 'rank'
FROM Scores;
