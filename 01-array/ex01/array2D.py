import numpy


def slice_me(family: list, start: int, end: int) -> list:
    """Slice a 2D array

    Args:
        family (list): 2D array
        start (int): Index to start
        end (int): Index to end

    Raises:
        TypeError: family must be a list(Matrix)
        TypeError: member(row) of family must be a list
        TypeError: start and end must be integers
        ValueError: The family must be a 2D array. Different length of rows

    Returns:
        list: _description_
    """
    # Validate the input
    if not isinstance(family, list):
        raise TypeError("family must be a list(Matrix)")
    for row in family:
        if not isinstance(row, list):
            raise TypeError("member(row) of family must be a list")
    if not isinstance(start, int) or not isinstance(end, int):
        raise TypeError("start and end must be integers")
    # Check if the family is 2D array(same length of rows)
    for i in range(len(family) - 1):
        if len(family[i]) != len(family[i + 1]):
            raise ValueError(
                "The family must be a 2D array. Different length\
              of rows"
            )
    # make the list in to numpy array
    family = numpy.array(family)
    # print shape
    print(f"My shape is     : {family.shape}")
    # slice the array
    sliced = family[start:end]
    # print shape
    print(f"My new shape is : {sliced.shape}")
    return sliced.tolist()
