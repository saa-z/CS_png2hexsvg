# test file checking every core function's behavior

import pytest
from PIL import Image

import png2hexsvg

# some formats available in pillow according to https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html
FORMATS = [("png", True), ("gif", False), ("jpeg", False)]


@pytest.mark.parametrize("extension, accepted", FORMATS)
def test_png2hexsvg_load_formats(tmp_path, extension, accepted):
    """Only PNG files are accepted,other formats raise ValueError"""
    path = tmp_path / f"input.{extension}"
    Image.new("RGB", (10, 10)).save(path)
    if accepted:
        assert png2hexsvg.load_image(path)
    else:
        with pytest.raises(ValueError):
            png2hexsvg.load_image(path)

def test_hexagon_centers_in_image():
    img = Image.new("RGB", (100, 50))
    size_small = [1,10,20]
    size_big = [50,100]
    for i in size_small:
        centers = png2hexsvg.hexagon_center(img, i)
        assert len(centers) > 0
        for cx, cy in centers:
            assert 0 <= cx < 100 and 0 <= cy < 50
    for i in size_big:
        with pytest.raises(ValueError):
            png2hexsvg.hexagon_center(img,i)