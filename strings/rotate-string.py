def rotateString(s: str, goal: str) -> bool:
    if len(s) != len(goal):
        return False

    n = len(s)
    new_string = s
    for _ in range(n):
        new_string = new_string[1:] + new_string[0]
        if new_string == goal:
            return True

    return False
