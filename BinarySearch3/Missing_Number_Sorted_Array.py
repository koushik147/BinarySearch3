def MissingElement(arr):
    l = 0
    h = len(arr)-1
    if arr[0]!=1:
        return 1
    if arr[-1]==len(arr):
        return len(arr)+1
        
    while l+1 != h:
        mid = l + (h-l) // 2
        if (arr[mid]-mid) == 1:
            l = mid
        else:
            h = mid
    return arr[l]+1
print(MissingElement([1,2,3,5,6]))