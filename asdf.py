class Solution:
    def findMedianSortedArrays(self, arr1, arr2):
        N1 = len(arr1)
        N2 = len(arr2)

        if N1 > N2:
            arr2, arr1 = arr2, arr1
            N1, N2 = N1, N2
        
        low = 0
        high = N1 * 2 #N1 is the shorter array. See above why *2

        while low <= high:
            mid1 = (low + high) // 2;   # Cut arr1
            mid2 = N1 + N2 - mid1;      # Find cut for arr2

            L1 = arr1[0] if (mid1 == 0) else arr1[(mid1-1)//2]	
            L2 = arr2[0] if (mid2 == 0) else arr2[(mid2-1)//2]     
            R1 = arr1[-1] if (mid1 == N1 * 2) else arr1[(mid1)//2] 
            R2 = arr2[-1] if (mid2 == N2 * 2) else arr2[(mid2)//2]
        
            if L1 > R2:
                high = mid1 - 1
            elif L2 > R1:
                low = mid1 + 1 
            else:
                return (max(L1, L2) + min(R1, R2)) / 2
        
arr1 = [1,3]
arr2 = [2]
x = Solution()
y= x.findMedianSortedArrays(arr1, arr2)
print(y)
