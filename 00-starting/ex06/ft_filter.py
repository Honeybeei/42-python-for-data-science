from typing import Callable, Iterable, TypeVar, List

T = TypeVar("T")


def ft_filter(function: Callable[[T], bool], iterable: Iterable[T]) -> List[T]:
    """Reimplemented filter function

    Args:
        function (Callable[[T], bool]): Function to be used to filter elements
        iterable (Iterable[T]): Iterable to filter

    Returns:
        List[T]: List of elements which function returns True
    """
    return [i for i in iterable if function(i)]
