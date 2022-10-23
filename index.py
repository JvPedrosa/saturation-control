from email.mime import image
from turtle import width
from PIL import Image
import numpy as np


def RGBtoHSV(r, g, b):

    # R, G, B são divididos por 255
    r = r / 255.0
    g = g / 255.0
    b = b / 255.0

    # h, s, v = matiz, saturação, brilho
    cmax = max(r, g, b)    # maximo de r, g, b
    cmin = min(r, g, b)    # minimo de r, g, b
    diff = cmax-cmin       # diferença de cmax e cmin.

    # se cmax e cmax são iguais então h = 0
    if cmax == cmin:
        h = 0

    # se cmax for igual a r então calcule h
    elif cmax == r:
        h = (60 * ((g - b) / diff) + 360) % 360

    # se cmax for igual a g então calcule h
    elif cmax == g:
        h = (60 * ((b - r) / diff) + 120) % 360

    # se cmax for igual a b então calcule h
    elif cmax == b:
        h = (60 * ((r - g) / diff) + 240) % 360

    # se cmax for igual a zero
    if cmax == 0:
        s = 0
    else:
        s = (diff / cmax) * 100

    # calcular v
    v = round(cmax * 100, 2)
    return h, s, v


im = Image.open(r"Shapes.png")

width = im.width
height = im.height
rgb = []

for i in range(width):
    linha = []
    for j in range(height):
        coordinate = i, j
        linha.append(im.getpixel(coordinate))
    rgb.append(linha)

r = rgb[100][100][0]
g = rgb[100][100][1]
b = rgb[100][100][2]

print(rgb[100][100])
print(RGBtoHSV(r, g, b))

im2 = Image.new('RGB', (width, height))

for i in range(width):
    for j in range(height):
        im2.putpixel((i, j), rgb[i][j])

# im2.show()
