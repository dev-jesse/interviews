def threeSum(self, nums: List[int]) -> List[List[int]]:
    # Sort the nums array so you can do classic two sum with two pointers
    nums.sort()
    res = []

    # Iterate the nums array for starting index, then use two pointers
    for start in range(len(nums) - 2):
        if start > 0 and nums[start] == nums[start - 1]: continue  # remove dupes
        left, right = start + 1, len(nums) - 1
        while left < right:
            # The numbers of the three indices should add up to 0
            if nums[left] + nums[right] < -nums[start]:
                left += 1
            elif nums[left] + nums[right] > -nums[start]:
                right -= 1
            else:
                if not res or res and res[-1] != [nums[start], nums[left], nums[right]]:
                    res.append([nums[start], nums[left], nums[right]])  # remove dupes
                left += 1
                right -= 1

    return res
