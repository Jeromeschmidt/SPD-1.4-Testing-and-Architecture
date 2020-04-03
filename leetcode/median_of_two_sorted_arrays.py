class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # find the middle element of 2 inputed arrays

        # take advantage of Python's Timsort
        new = sorted(nums1 + nums2)

        #find median of new sorted array, depending on length of array(odd or even length)
        if len(new) % 2 == 1:
            return (new[int(len(new)/2)])
        else:
            low = int((len(new)-1)/2)
            return ((new[low] + new[low + 1])/2)    
