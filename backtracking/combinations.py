def combine(self, n: int, k: int) -> List[List[int]]:
    results = []
    self.bt(range(1, n + 1), k, [], results)
    return results


def bt(self, nums, k, path, results):
    if len(path) == k:
        results.append(path)
        return

    for i in range(len(nums)):
        self.bt(nums[i + 1:], k, path + [nums[i]], results)
