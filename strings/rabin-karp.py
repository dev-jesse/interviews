def str_str2(source: str, target: str) -> int:
        n, m = len(source), len(target)
        if m == 0:
            return 0
        
        target_hash = source_hash = 0
        top_power = 1
        hash_size = 1000007

        for i in range(m - 1):
            top_power = (top_power * 31) % hash_size
            target_hash = (target_hash * 31 + ord(target[i])) % hash_size
        target_hash = (target_hash * 31 + ord(target[m - 1])) % hash_size

        for i in range(n):
            if i >= m:
                source_hash = source_hash - (top_power * ord(source[i - m])) % hash_size
            source_hash = (source_hash * 31 + ord(source[i])) % hash_size
            if source_hash == target_hash and source[i - m + 1: i + 1] == target:
                return i - m + 1

        return -1
