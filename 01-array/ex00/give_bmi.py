import numpy


def give_bmi(
    height: list[int | float],
    weight: list[int | float],
) -> list[int | float]:
    """Calculate the BMI using the formula: weight / height^2

    Args:
        height (list[int  |  float]): array of heights
        weight (list[int  |  float]): array of weights

    Raises:
        ValueError: empty lists
        ValueError: lists with different lengths
        ValueError: lists with non-numeric values
        ValueError: lists with zero or negative values

    Returns:
        list[int | float]: array of BMI values
    """
    # check if the lists are empty
    if not height or not weight:
        raise ValueError("The lists should not be empty")
    # check if the length of the two lists are the same
    if len(height) != len(weight):
        raise ValueError("The lists should have the same length")
    # check if the length of the two lists contains only numbers
    for value in height + weight:
        if not isinstance(value, (int, float)):
            raise ValueError("The lists should contain only numbers")
        elif value <= 0:
            raise ValueError("The lists should contain only positive numbers")
    # calculate BMI using numpy
    bmi = numpy.array(weight) / (numpy.array(height) ** 2)
    return bmi.tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Check if the BMI is above a certain limit

    Args:
        bmi (list[int  |  float]): array of BMI values
        limit (int): the limit to check against

    Returns:
        list[bool]: array of boolean values
    """
    return [value > limit for value in bmi]
