def subsets(self, nums: List[int]) -> List[List[int]]:
    nums.sort()
    results = []
    self.bt(nums, [], results)
    return results


def bt(self, nums, path, results):
    results.append(path)
    for i in range(len(nums)):
        self.bt(nums[i + 1:], path + [nums[i]], results)
