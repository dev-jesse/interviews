def permuteUnique(self, nums: List[int]) -> List[List[int]]:
    nums.sort()
    results = []
    self.bt(nums, set(), [], results)
    return results


def bt(self, nums, seen, path, results):
    if len(nums) == len(path):
        results.append(path)
        return

    for i in range(len(nums)):
        if i in seen:
            continue
        if i > 0 and i - 1 not in seen and nums[i] == nums[i - 1]:
            continue
        seen.add(i)
        self.bt(nums, seen, path + [nums[i]], results)
        seen.remove(i)
