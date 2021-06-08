"""
Written by: Enzo Villarama
UPI: evil629

Contents:

These are functions used for converting the image to greyscale

"""


def createInitializedGreyscalePixelArray(image_width, image_height, initValue=0):

    new_array = [[initValue for x in range(image_width)] for y in range(image_height)]
    return new_array


def greyscale(r, g, b, w, h):

    image = []

    for y in range(h):

        row = []

        for x in range(w):

            triple = []
            triple.append(r[y][x])
            triple.append(g[y][x])
            triple.append(b[y][x])
            row.append(triple)

        image.append(row)

    return image


def computeGreyscale(r, g, b, w, h):
    # g = 0.299 * r + 0.587 * g + 0.114 * b

    image = createInitializedGreyscalePixelArray(w, h)

    for i in range(h):

        for j in range(w):

            red = r[i][j] * 0.299
            green = g[i][j] * 0.587
            blue = b[i][j] * 0.114

            image[i][j] = round(red + green + blue)

    return image


# Not used
def computeMinMax(array, image_height):

    minMax = []
    temp = []

    for i in range(image_height):

        temp.append(min(array[i]))
        temp.append(max(array[i]))

    minMax.append(min(temp))
    minMax.append(max(temp))

    return minMax


# Not used
def scale0to255andQuantize(image, image_width, image_height):

    minMax = computeMinMax(image, image_height)

    grey = []

    for i in range(image_height):

        temp = []

        for j in range(image_width):

            value = (image[i][j] - minMax[0])
            dnom = minMax[1] - minMax[0]

            if dnom == 0:
                temp.append(0)

            else:
                p2 = 255 / dnom
                v = value * p2

                temp.append(v)

        grey.append(temp)

    return grey
