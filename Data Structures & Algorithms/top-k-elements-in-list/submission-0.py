class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        Understand- Given an array nums, return the k most frequent elements in an array
            inputs- nums , k
            outputs- list of k most frequent nums
        Plan-
            count the frequency of each number in nums array
            using bucket sort map the i(count) to the values from the num array

        Implement-


        '''
        counter = {}
        freq = [[] for i in range(len(nums)+ 1)] # lists of empty lists thats the same size as input array, index is freqency of an element
                                                # value is the value that occurs tha particular index of times

        for num in nums: # frequency of each number stored in counter
            counter[num] = 1 + counter.get(num,0)

        for num, c in counter.items():  # going through each value counted
            freq[c].append(num) # at index value of c, the num occurs c number of times

        
        result = []

        for i in range(len(freq)-1, 0, -1): # in descending order as we are starting with the numbers that are the most frequent
            for num in freq[i]:
                result.append(num) # this appends from the greatest frequency to the least
                if len(result) == k: # so whenever the length of result == k, then we have k most frequent elements and the rest are irrelevant
                    return result 


        #time and space :O(N)