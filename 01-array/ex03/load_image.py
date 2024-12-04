import numpy
import cv2


def ft_load(path: str) -> numpy.ndarray:
    """Load an image from a file

    Args:
        path (str): The path to the image file

    Raises:
        Exception: If the image cannot be loaded

    Returns:
        numpy.ndarray: The image as a NumPy array
    """
    image = cv2.imread(path)
    if image is None:
        raise Exception("Error loading image")
    print(f"The shape of image is: {image.shape}")
    return image
