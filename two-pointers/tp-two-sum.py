def two_sum(numbers: List[int], target: int) -> List[int]:
        mapped = [(e, i) for i, e in enumerate(numbers)]
        mapped.sort()

        left, right = 0, len(numbers) - 1
        while left < right:
            if mapped[left][0] + mapped[right][0] < target:
                left += 1
            elif mapped[left][0] + mapped[right][0] > target:
                right -= 1
            else:
                return sorted([mapped[left][1], mapped[right][1]])

        return -1, -1
