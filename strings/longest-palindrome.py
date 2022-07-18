def longestPalindrome(s: str) -> int:
    letters = set()
    count = 0
    for char in s:
        if char not in letters:
            letters.add(char)
        else:
            letters.remove(char)
            count += 1

    return 2 * count if not letters else 2 * count + 1
