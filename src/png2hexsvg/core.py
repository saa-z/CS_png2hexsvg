# file with every needed function
from PIL import Image


def load_image(path):
    """
    Opens a PNG picture

    :param path: PNG image path
    :return: the opened PNG image
    :raises ValueError: if the file is not a PNG picture
    """

    img = Image.open(path)
    if img.format != "PNG":
        raise ValueError("Only PNG format supported")
    return img
