def permute(nums):
    if len(nums) == 0:
        return []
    if len(nums) == 1:
        return [nums]
    else:
        output = []
        for i, num in enumerate(nums):
            new_nums = nums[:i] + nums[i+1:]
            for perm in permute(new_nums):
                output.append([num]+perm)
        return output

def permute_yield(nums):
    if len(nums) == 0:
        yield []
    if len(nums) == 1:
        yield nums
    else:
        for i, num in enumerate(nums):
            new_nums = nums[:i] + nums[i+1:]
            for perm in permute(new_nums):
                yield [num]+perm

nums = list('123')
print(permute(nums))
# for py in permute_yield(nums):
#     print(py)