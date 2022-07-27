def combinationSum3(self, k: int, n: int) -> List[List[int]]:
    results = []
    self.bt(range(1, 10), k, n, 0, [], results)
    return results


def bt(self, nums, k, n, index, path, results):
    if k == 0 and n == 0:
        results.append(path)
        return
    if k == 0 or n < 0:
        return

    for i in range(index, len(nums)):
        self.bt(nums, k - 1, n - nums[i], i + 1, path + [nums[i]], results)
