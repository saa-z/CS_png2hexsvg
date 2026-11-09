# file with every needed function
from PIL import Image


# Image functions
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

#Hexagonal Grid
def hexagon_center(img, size):
    """Compute the centers of flat-top hexagons covering the picture.

    :param img: opened picture (PIL Image)
    :param size: hexagon size in pixels (distance from center to corner)
    :return: list of hexagon centers [cx, cy]
    """
    w, h = img.size
    dx, dy = 1.5 * size, (3**0.5) * size
    nb_cols = int(w / dx)
    nb_rows = int(h / dy)

    hexagon_centers = []
    for row in range(nb_rows):
        for col in range(nb_cols):
            cx, cy = col * dx, row * dy
            if col % 2 == 1:
                cy += dy / 2  # odd columns shifted down
            hexagon_centers.append([int(cx), int(cy)])
    return hexagon_centers

