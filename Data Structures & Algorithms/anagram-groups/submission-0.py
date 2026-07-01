class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        Understand- given an array of strs, group all the anagrams into sublists in any order
            input - strs ; list of words
            output - anagram_list 
        Plan-
            26 unique characters(a-z)
            create an array count(a-z)
            create an hashmap with the value being the anagram
        Implement- 
        '''

        res = defaultdict(list) # mapping charCount of each string to list of anagrams

        for string in strs:
            count = [0] * 26 # a-z 

            for char in string:
                count[ord(char) - ord("a")] += 1

            res[tuple(count)].append(string)

        
        return list(res.values())

        #O(m*n) m = num of strings# n = length of each string