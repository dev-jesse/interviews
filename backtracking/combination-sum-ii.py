def combinationSum2(candidates: List[int], target: int) -> List[List[int]]:
    candidates.sort()
    results = []
    bt(candidates, target, 0, [], results)
    return results


def bt(candidates, target, index, path, results):
    if target == 0:
        results.append(path)
        return
    if target < 0:
        return

    for i in range(index, len(candidates)):
        if i > index and candidates[i] == candidates[i - 1]:
            continue
        bt(candidates, target - candidates[i], i + 1, path + [candidates[i]], results)
