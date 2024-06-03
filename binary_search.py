def binary_search(arr, target):
    left = 0
    right = len(arr)-1
    mid = 0
    while left <= right:
        mid = (left+right)//2
        if arr[mid] < target:
            left = mid+1          
        elif arr[mid] > target:
            right = mid-1            
        else:
            return arr[mid]
    return -1
target = 19
arr = [1,3,5,7,9,11,13,15,17,19]
print(binary_search(arr, target))