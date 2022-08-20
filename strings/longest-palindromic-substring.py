def longestPalindrome(s: str) -> str:
    res = ''
    for i in range(len(s)):
        # Odd case: Such as 'aba'
        tmp = extend_out(s, i, i)
        if len(tmp) > len(res): res = tmp

        # Even case: Such as 'abba'
        tmp = extend_out(s, i, i + 1)
        if len(tmp) > len(res): res = tmp

    return res


def extend_out(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1

    return s[left + 1: right]
