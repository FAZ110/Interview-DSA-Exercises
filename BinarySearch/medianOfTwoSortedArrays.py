'''
You are given two integer arrays nums1 and nums2 of size m and n 
respectively, where each is sorted in ascending order. Return the 
median value among all elements of the two arrays.

Your solution must run in O(log(m+n))O(log(m+n)) time.
'''

# EXAMPLES

# Input: nums1 = [1,2], nums2 = [3]
# Output: 2.0

# Input: nums1 = [1,3], nums2 = [2,4]
# Output: 2.5

'''
To find the median in O(log(min(m,n))), we use binary search to find 
a "cut" in the smaller array that simultaneously determines a "cut" in 
the larger array.

The goal is to partition both arrays such that the combined left side 
and the combined right side each contain half of the total elements. 
We know the partition is correct when the largest elements on the left 
side of both cuts are less than or equal to the smallest elements on 
the right side of both cuts.

Because the arrays are already sorted, we only need to check these 
four boundary values: if the "cross-condition" (L1≤R2 and L2≤R1) is 
met, the median is simply the maximum of the left values (and the minimum of the right values if the total count is even).

Would you like me to provide a step-by-step dry run using a specific 
pair of arrays?
'''

def findMedianSortedArrays(nums1, nums2):
    # ensure nums1 is smaller array to optimize binary search
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    
    m,n = len(nums1), len(nums2)
    low, high = 0, m

    while low <= high:
        # partition index for nums1
        partition1 = (low + high) // 2
        # partition index for nums2
        partition2 = (m + n + 1) // 2 - partition1

        # Values at the edges of the partitions (with infinity handling)
        l1 = nums1[partition1 - 1] if partition1 > 0 else float('-inf')
        r1 = nums1[partition1] if partition1 < m else float('inf')
        
        l2 = nums2[partition2 - 1] if partition2 > 0 else float('-inf')
        r2 = nums2[partition2] if partition2 < n else float('inf')

        # Check if we found the correct partition
        if l1 <= r2 and l2 <= r1:
            # If total elements are odd
            if (m+n) % 2 == 1:
                return float(max(l1, l2))
            # If total elements are even
            else:
                return (max(l1,l2) + min(r1,r2))/2.0
        elif l1 > l2:
            # We are too far right in nums1, move left
            high = partition1 - 1
        else:
            # We are too far left in nums1, move right
            low = partition1 + 1
    return 0.0


nums1 = [1,3]
nums2 = [2,4]
print(findMedianSortedArrays(nums1, nums2))


