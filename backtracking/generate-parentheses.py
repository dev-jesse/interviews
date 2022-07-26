def generateParenthesis(n):
    results = []
    bt(n, 0, 0, "", results)
    return results


def bt(n, opn, close, path, results):
    if len(path) == 2 * n:
        results.append(path)
        return

    if opn < n:
        bt(n, opn + 1, close, path + "(", results)
    if close < opn:
        bt(n, opn, close + 1, path + ")", results)
