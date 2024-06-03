# def quicksort(nums, l, r, p):
#     while l<=r:
#         while nums[l] <= nums[p]:
#             l += 1
#         while nums[r] >= nums[p]:
#             r -= 1
#         nums[l], nums[r] = nums[r], nums[l]
#     nums[r], nums[p] = nums[p], nums[r]
#     quicksort(nums[:r-1], 0, r, r)
#     quicksort(nums[r:], 0, len(nums[r:])-1, len(nums[r:])-1)
#     return nums

def quicksort(array):
    """Sort the array by using quicksort."""

    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        # Don't forget to return something!
        return quicksort(less)+equal+quicksort(greater)  # Just use the + operator to join lists
    # Note that you want equal ^^^^^ not pivot
    else:  # You need to handle the part at the end of the recursion - when you only have one element in your array, just return the array.
        return array
    

nums = [3,5,8,1,2,9,4,7,6]
# nums = [12,4,5,6,7,3,1,15]

print(quicksort(nums))