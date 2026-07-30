class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        Understand- return the index of the target num if its in the array
            input - nums array and target
            output - the index of target or -1 if not found
            constraints - has to be in O(log n ) time
        Plan-
        if array is empty 
            return -1
        create left and right pointer for binary search
        iterate while left is less then equal right pointer:
            initilize the mid point formula is mid = (left + right) // 2
            if nums[mid] == target:
                return mid # if mid is target we can return the index early 
            

        Implement
        '''

        if not nums:
            return -1

        left, right = 0 , len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:

                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:

                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1 
