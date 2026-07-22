class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        Understand- Return the length of longest substring containing the same letter 
            you can get after performing atmost k operations
            input : string s and int k
            output : int; length of longest substring
        Plan-
            left = 0
            counter = {}

            for right in range(len(s)):
                add s[right] to counter

                check while the window is invalid: windowlen - the count of most common letter is greater than k
                    and also remove the left pointer char from counter
                    increment left pointer
                get max size of window 

            return max_size of window
        Implement- 
        '''
        #len of window is r-l + 1
        l = 0
        counter = {}
        max_length = 0

        for r in range(len(s)):
            counter[s[r]] = 1 + counter.get(s[r], 0)
            '''
            if s[r] not in counter:
                s[r] = 1
            else:
                s[r] += 1
            '''

            while (r - l + 1) - max(counter.values()) > k: #meaning window is invalid
                counter[s[l]] -= 1
                l += 1

            max_length = max(max_length, r - l + 1)

        return max_length