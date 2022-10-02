class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = self.binarysearch(nums,target,True) # searching the left part of nums
        right = self.binarysearch(nums,target,False) # searching the right part of nums
        
        return [left,right] # returning both left and right in an array
    
    def binarysearch(self,nums,target,flag):
        l = 0 # assigning to index 0
        h = len(nums) - 1 # assigning to last index 
        i=-1
        while(l<=h): # until l less than h
            mid = l + (h-l) // 2 # finding mid value
            
            if nums[mid] < target: # if mid less than target
                l = mid + 1
            elif nums[mid] > target: # if mid greater than target
                h = mid - 1
            else: 
                i=mid # assigning i to mid value
                if flag: # if flag is true
                    h=mid-1
                else: # if flag is false
                    l=mid+1
        return i