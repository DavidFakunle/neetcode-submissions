class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        Understand - Given an array sorted in ascending order that has been rotated , find the min
                    number in the sorted array
                input - nums array
                output - the minimum number in the array
                constraints - has to be in O(log n) time so binary search
        Plan-
            create a left and right pointer
            while left is less than or equal to right
                define middle as left + right // 2 to get middle number 
                if the middle number is greater than the right
                    this means the smallest value can be found on the rightside
                else:
                    its on the left side, so move the right value to equal mid
            return right value
        Implement-
        '''
        left, right = 0 , len(nums) - 1

        while left < right:
            mid = (left + right ) // 2
            if nums[mid] >= nums[right]:# the minimum value appears on the rightside of the array
                left = mid + 1
            else:
                right = mid # else it appears on the left side , and the min value could be middle value so keep it 

        return nums[right]
                 
