def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
        results = []
        bt(candidates, target, 0, [], results)
        return results
    
    
def bt(candidates, target, index, path, results):
    if target == 0:
        results.append(list(path))
        return
    if target < 0:
        return

    for i in range(index, len(candidates)):
        bt(candidates, target - candidates[i], i, path + [candidates[i]], results)
