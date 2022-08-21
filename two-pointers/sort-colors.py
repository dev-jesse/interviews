def sortColors(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    # Use the dutch partition algorithm
    red, white, blue = 0, 0, len(nums) - 1

    # Need to use <= since when white == blue, there may a red that need be shifted
    # For example: Run through the input [2, 0, 1] (will return [1, 0 , 2])
    while white <= blue:
        if nums[white] == 0:
            nums[red], nums[white] = nums[white], nums[red]
            white += 1
            # Also increment red, since we have 0 there, no need to check for another swap
            red += 1
        elif nums[white] == 1:
            white += 1
        else:
            nums[white], nums[blue] = nums[blue], nums[white]
            blue -= 1
            # Cannot decrement white since it may have swapped with another blue
