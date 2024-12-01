def count_in_list(lst: list, target: str) -> int:
    """This function counts the number of times a target string appears in a
    list.

    Args:
        lst (list): List to be searched
        target (str): Target string to search for

    Returns:
        int: The number of times the target string appears in the list
    """
    count = 0
    for item in lst:
        if item == target:
            count += 1
    return count
