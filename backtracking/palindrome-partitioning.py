def partition(self, s: str) -> List[List[str]]:
    results = []
    self.bt(s, [], results)
    return results


def bt(self, s, path, results):
    if not s:
        results.append(path)
        return

    for i in range(1, len(s) + 1):
        if not self.is_palindrome(s[:i]):
            continue    
        self.bt(s[i:], path + [s[:i]], results)


def is_palindrome(self, string):
    return string == string[::-1]
