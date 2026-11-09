# file with every needed function
import math

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

#V1 no check on the compatability between image size and hexagonal size
def hexagon_center(img, size):
    """Compute the centers of flat-top hexagons covering the picture.

    :param img: opened picture (PIL Image)
    :param size: hexagon size in pixels (distance from center to corner)
    :return: list of hexagon centers [cx, cy]
    """
    w, h = img.size
    w, h = img.size
    dx, dy = 1.5 * size, (3**0.5) * size
    nb_cols = int(w / dx)
    nb_rows = int(h / dy)
    if nb_cols ==0 or nb_rows ==0:
        raise ValueError(f"Hexagon size {size} too big for a {w}x{h} picture")
    hexagon_centers = []
    for row in range(nb_rows):
        for col in range(nb_cols):
            cx, cy = col * dx, row * dy
            if col % 2 == 1:
                cy += dy / 2  # odd columns shifted down
                hexagon_centers.append([int(cx), int(cy)])
    return hexagon_centers

def hexagon_corners(center, size):
    """Compute the 6 corners of a flat-top hexagon.

    :param center: coordinates [cx, cy] of the hexagon center
    :param size: hexagon size in pixels (distance from center to corner)
    :return: list of the 6 corners (x, y)
    """
    corners = []
    for i in range(6):
        angle = math.radians(60 * i)
        x = center[0] + size * math.cos(angle)
        y = center[1] + size * math.sin(angle)
        corners.append((x, y))
    return corners