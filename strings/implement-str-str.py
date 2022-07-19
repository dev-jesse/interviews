def str_str(source: str, target: str) -> int:
    if not target:
        return 0
    if not source:
        return -1

    for i in range(len(source)):
        if i + len(target) > len(source):
            break

        for j in range(len(target)):
            if source[i + j] != target[j]:
                break
            if j == len(target) - 1:
                return i
    return -1
