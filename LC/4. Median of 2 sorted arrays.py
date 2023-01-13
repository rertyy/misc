##Median of 2 sorted arrays
## https://leetcode.com/problems/median-of-two-sorted-arrays/solutions/2471/very-concise-o-log-min-m-n-iterative-solution-with-detailed-explanation/
## In the 2 arrays below, the median is (5+6)/2
##
## arr1 *1*3* 5/ 7*9*11*    L1 = 5, R1 = 7, N1 = 6, Ni1 = 13, C1 = N1+N2-k2 = 6
## arr2  *2*4 /6 *8*        L2 = 4, R2 = 6, N2 = 4, Ni2 = 9,  C2 = 4
##
## len2 <= len1
## L is left of slice, R is right of slice
## L1 = A1[(C1-1)//2]; R1 = A1[C1//2];
## L2 = A2[(C2-1)//2]; R2 = A2[C2//2];
## N is length
## Ni is number of positions including blanks
## C is cut
##
## Imagine positions before and after each array i.e. *1*3*5*7*9*11*, so N1+1 positions including the numbers
## Since median has half numbers on left and half numbers on right,
## N1+N2-C2 = C1, where k are the positions of cuts
##
## Since both arrays are sorted, everything on the left of each is always less
## than everything on the right.
## So just find when L1<=R2 and R2<=R1
## Then do binary search on the smaller array until line above is true
## if L1 > R2, then C1 to move left i.e. C2 move right
## if L2 > R1, then C2 move to left

#Why high = N2 * 2?
#The total length of the inputs (i.e. N1 + N2) could be an odd or even number.
#Normally these two cases need to processed differently.
#In this algorithm, however, I instead consider cut positions
#(i.e. elements or spaces between/around elements),
#which is always an even number.
#On array 2, there are 2N2 + 1 such positions indexed from 0 to 2N2.

#i.e. there are 2N+1 positions, leading to 2N indices


def median(arr1, arr2):
    N1 = len(arr1)
    N2 = len(arr2)
    print("llamaduck")
##    if N1 > N2: #Make N1 the shorter array
##        return median(arr2, arr1)
    if N1 > N2:
        arr2, arr1 = arr2, arr1
        N1, N2 = N1, N2
    
    low = 0
    high = N1 * 2 #N1 is the shorter array. See above why *2

    while low <= high:
        mid1 = (low + high) // 2;   # Cut arr1
        mid2 = N1 + N2 - mid1;      # Find cut for arr2

        L1 = arr1[0] if (mid1 == 0) else arr1[(mid1-1)//2]	# Get L1, R1, L2, R2 respectively
        L2 = arr2[0] if (mid2 == 0) else arr2[(mid2-1)//2]      # if mid is 0 index, then 0 index is ans
        R1 = arr1[-1] if (mid1 == N1 * 2) else arr1[(mid1)//2]  # if mid is last index, then last index is ans
        R2 = arr2[-1] if (mid2 == N2 * 2) else arr2[(mid2)//2]
    
        if L1 > R2:
            high = mid1 - 1
        elif L2 > R1:
            low = mid1 + 1 
        else:
            return (max(L1, L2) + min(R1, R2)) / 2
    
  

#Clearer version without using *2
def medianV2(arr1, arr2):
    N1 = len(arr1)
    N2 = len(arr2)
    
    if N1 > N2: 
        return medianV2(arr2, arr1)
    
    low = 0
    high = N1 #N1 is the shorter array.

    while low <= high:
        mid1 = (low + high) // 2;   # Cut arr2
        mid2 = (N1 + N2)//2 - mid1;      # Find cut for arr1
        
        L1 = arr1[0] if (mid1 == 0) else arr1[(mid1-1)]	# Get L1, R1, L2, R2 respectively
        L2 = arr2[0] if (mid2 == 0) else arr2[(mid2-1)]      # if mid is 0 index, then 0 index is ans
        R1 = arr1[-1] if (mid1 == N1) else arr1[(mid1)]  # if mid is last index, then last index is ans
        R2 = arr2[-1] if (mid2 == N2) else arr2[(mid2)]
    
        if L1 > R2:
            high = mid1 - 1 #shift C2 to the left by binary searching arr2 on the left side
            
        elif L2 > R1:
            low = mid1 + 1 #shift C2 to the right by binary searching arr2 on the right side
        else:
            return (max(L1, L2) + min(R1, R2)) / 2
    
    


        





arr1 = [1,3]
arr2 = [2]
x = median(arr1, arr2)
print(x)
