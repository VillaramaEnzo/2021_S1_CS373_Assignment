import math


def computeGradient(horizontal, vertical):

    gradient = []

    for h, v in zip(horizontal, vertical):

        t = []

        for h1, v1 in zip(h, v):

            t.append(math.sqrt(math.pow(h1, 2) + math.pow(v1, 2)))

        gradient.append(t)

    return gradient


def computeVerticalEdges(pixel_array, image_width, image_height):

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

            pos = pixel_array[i - 1][j + 1] + (2 * pixel_array[i][j + 1]) + pixel_array[i + 1][j + 1]
            neg = (-1 * pixel_array[i - 1][j - 1]) + (-2 * pixel_array[i][j - 1]) + (-1 * pixel_array[i + 1][j - 1])

            val = - (pos + neg) / 8

            temp.append(val)

        lst.append(temp)

    return lst


def computeHorizontalEdges(pixel_array, image_width, image_height):

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

            pos = pixel_array[i - 1][j - 1] + (2 * pixel_array[i - 1][j]) + pixel_array[i - 1][j + 1]
            neg = (-1 * pixel_array[i + 1][j - 1]) + (-2 * pixel_array[i + 1][j]) + (-1 * pixel_array[i + 1][j + 1])

            val = (pos + neg) / 8

            temp.append(val)

        lst.append(temp)

    return lst
