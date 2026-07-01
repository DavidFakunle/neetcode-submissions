class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        Understand- given an array of strs, group all the anagrams into sublists in any order
            input - strs ; list of words
            output - anagram_list 
        Plan-
            create a result dicto for mapping the charCount of each string to string in strs

            loop through strs array
                for each string create count array

                for each char in current string
                    update the frequency in count array

                
            then append to result: Anagrams will group by default because they share the same tuple key

            return only the values or result dict in list format
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