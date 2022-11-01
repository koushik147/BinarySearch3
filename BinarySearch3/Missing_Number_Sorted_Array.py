#TimeComplexity: O(log n)
#SpaceComplexity: O(1)
def MissingElement(arr):
    l = 0 # setting to initial pointer
    h = len(arr)-1 # setting to last pointer
    if arr[0]!=1: # if first value in array is not equal to 1
        return 1
    if arr[-1]==len(arr): # if array of last element is equal to length of array
        return len(arr)+1 
        
    while l+1 != h: # until start pointer is not equal to last pointer
        mid = l + (h-l) // 2 # finding the mid value
        if (arr[mid]-mid) == 1: # value minus index
            l = mid
        else: 
            h = mid
    return arr[l]+1 # returning the next value of lth pointer
print(MissingElement([1,2,3,5,6]))
