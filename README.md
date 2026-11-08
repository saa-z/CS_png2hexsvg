# Final project of Computer Science refresher 
### Azariouh Salwa - M1DS

## About

Convert a PNG picture into an SVG file made of hexagons,
each filled with the average color of the pixels it covers.

![hexagon_img1](img_1.png)

## Development workflow

- **Test-Driven Development**: each feature starts with a failing test
- **GitHub issues** to plan every feature and closed by commits
- **One branch per feature**, merged into `main`
- **Conventional commits** naming
- **CI/CD with GitHub Actions**: lint and tests on every push, publication to PyPI
- **Marimo notebooks** with a file picker and dynamic parameter (e.g: hexagon size)

## Resources and advised steps (cf [instructions](https://docs.numerique.gouv.fr/docs/c54e8f2e-008f-4929-b7ff-dd4d72a0c1a8/))

- Load the input picture using `Image.open(INPUT_FILENAME)` from the [PILuv  library](https://he-arc.github.io/livre-python/pillow/index.html),\
Iterate through some of the pixels of the input image using a [hexagonal grid](https://www.redblobgames.com/grids/hexagons/)
- [Sample the color](https://www.geeksforgeeks.org/python/python-pil-getpixel-method/) of each hexagon (by iterating over tens of pixels per hexagon)
- Create an [SVG hexagon](https://www.tutorialscampus.com/html5/svg-draw-hexagon.htm) with the average color sampled from the input file 
- Write the resulting output picture in an [.svg file](https://www.w3.org/TR/SVG2/struct.html) 

## Useful library 
- pillow
- marimo
- numpy
- pytest
- ruff
