"""
Written by: Enzo Villarama
UPI: evil629

Contents:

These functions are used for applying filters to the image

~ Includes ~
- Guassian Filter sobel
- Mean Filter sobel

-- All are 3x3 sobels currently

"""


def guassianFilter(pixel_array, image_width, image_height):

    lst = []

    if image_width == 1 and image_height == 1:

        return pixel_array

    pixel_array.insert(0, pixel_array[0].copy())
    pixel_array.append(pixel_array[image_height].copy())

    for i in range(image_height + 2):

        pixel_array[i].insert(0, pixel_array[i][0])
        pixel_array[i].append(pixel_array[i][-1])

    for i in range(image_height + 2):

        if i == 0 or (i == image_height + 1):

            continue

        temp = []

        for j in range(image_width + 2):

            if j == 0 or (j == image_width + 1):

                continue

            p1 = pixel_array[i - 1][j - 1] + (pixel_array[i - 1][j] * 2) + pixel_array[i - 1][j + 1]
            p2 = (pixel_array[i][j - 1] * 2) + (pixel_array[i][j] * 4) + (pixel_array[i][j + 1] * 2)
            p3 = pixel_array[i + 1][j - 1] + (pixel_array[i + 1][j] * 2) + pixel_array[i + 1][j + 1]

            val = (p1 + p2 + p3) / 16

            temp.append(val)

        lst.append(temp)

    return lst


def meanFilter(pixel_array, image_width, image_height):

    lst = []

    for i in range(image_height):

        if i == 0 or (i == image_height - 1):

            lst.append([0.000] * image_width)

            continue

        temp = []

        for j in range(image_width):

            if j == 0 or (j == image_width - 1):

                temp.append(0.000)

                continue

            p1 = pixel_array[i - 1][j - 1] + pixel_array[i - 1][j] + pixel_array[i - 1][j + 1]
            p2 = pixel_array[i][j - 1] + pixel_array[i][j] + pixel_array[i][j + 1]
            p3 = pixel_array[i + 1][j - 1] + pixel_array[i + 1][j] + pixel_array[i + 1][j + 1]

            val = (p1 + p2 + p3) / 9

            temp.append(val)

        lst.append(temp)

    return lst
