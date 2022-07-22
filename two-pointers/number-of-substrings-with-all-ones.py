def string_count(str: str) -> int:
    # Clever solution using the formula: n*(n+1) / 2
    # Notice: '1' -> 1 substrings
    #         '11' -> 3 substrings (1 + 2)
    #         '111' -> 6 substrings (1 + 2 + 3)
    # Therefore, just use sliding window to get max sequences

    n = len(str)
    i = ans = 0
    for j in range(n + 1):
        if j == n or str[j] == '0':
            ans += (j - i) * (j - i + 1) // 2
            i = j + 1

    return ans
