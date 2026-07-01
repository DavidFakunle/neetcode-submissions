class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        Understand- return true if s and t are anagrams and false if not
            input - string s and t
            output - true if Anagram false if not
        Plan-
            check if they are the same length first

            make a dictionary to count the frequency of letters in string s

            then loop through t string
                if t char is in the s frequency dictionary 
                    subtract it by 1
                    if s[char] == 0:
                        del s[char]
                else:
                    return False

            return if frequency dictionary is empty 
        Implement-
        '''

        if len(s) != len(t):
            return False

        s_count = {}

        for let in s:
            if let in s_count:
                s_count[let] += 1
            else:
                s_count[let] = 1


        for let in t:
            if let in s_count:
                s_count[let] -= 1
                if s_count[let] == 0:
                    del s_count[let]
            else:
                return False

        return len(s_count) == 0

