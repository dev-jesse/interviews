def maxArea(height: List[int]) -> int:
    # Start with the widest container and move in
    left, right = 0, len(height) - 1
    res = 0

    # Calculate how much water in each container
    while left < right:
        # Area = Base x Height, where you take the min height to prevent overfill
        res = max(res, min(height[left], height[right]) * (right - left))
        # Move the min height in to attempt to make larger area of water
        if height[left] < height[right]: left += 1
        else: right -= 1

    return res
