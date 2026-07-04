class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        Understand- Given an integer nums, return the length of the longest consecutive sequence
                    of numbers that can be formed
                    input: nums array
                    output : length of longest consecutive sequence
                    constraints: Has to be in O(n) complexity
        Plan-
            turn into a set
            we can consider a number a sequence if num - 1 does not exist
            max_length = 0
            for num in nums:
                if num - 1 not in nums:
                    start = num # found our starting sequence
                    length = 0
                    while start + 1 in nums: # now check if the next consecutive number in nums
                        length += 1 # so we increment or length
                        start = start + 1 # update our start 
                    
                    max_length = max(length, max_length)

            return max_length
            Time and memory = O(N)
        Implement-
        '''

        max_length = 0
        numSet = set(nums)
        for num in numSet:
            if num - 1 not in numSet:
                start = num
                length = 1

                while start + 1 in numSet:
                    length += 1
                    start = start + 1
                
                max_length = max(length, max_length)

        return max_length