def removeDuplicates(nums: List[int]) -> int:
    # Keep track of where you want to place next number with left pointer
    n = len(nums)
    i = 0

    # Iterate the right pointer and ignore the dupes
    for j in range(1, n):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]

    return i + 1
