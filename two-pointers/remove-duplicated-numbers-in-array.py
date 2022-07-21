def deduplication(self, nums: List[int]) -> int:
    if not nums:
        return 0 

    nums.sort()
    j = 0
    for i in range(len(nums) - 1):
        if nums[i] != nums[i + 1]:
            nums[j] = nums[i]
            j += 1

    nums[j] = nums[-1]
    return (j + 1)
