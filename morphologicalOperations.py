import copy


def computeErosion(pixel_array, image_width, image_height):
    lst = []

    for i in range(image_height):

        temp = []

        for j in range(image_width):

            if (i == 0 or j == 0 or i == image_height - 1 or j == image_width - 1):
                temp.append(0)

            elif ((pixel_array[i - 1][j - 1] == 1
                    and pixel_array[i - 1][j] == 1
                    and pixel_array[i - 1][j + 1] == 1
                    and pixel_array[i][j - 1] == 1
                    and pixel_array[i][j] == 1
                    and pixel_array[i][j + 1] == 1
                    and pixel_array[i + 1][j - 1] == 1
                    and pixel_array[i + 1][j] == 1
                    and pixel_array[i + 1][j + 1] == 1)
                    or
                    (pixel_array[i - 1][j - 1] == 255
                        and pixel_array[i - 1][j] == 255
                        and pixel_array[i - 1][j + 1] == 255
                        and pixel_array[i][j - 1] == 255
                        and pixel_array[i][j] == 255
                        and pixel_array[i][j+1] == 255
                        and pixel_array[i+1][j-1] == 255
                        and pixel_array[i+1][j] == 255
                        and pixel_array[i+1][j+1] == 255)):

                temp.append(1)

            else:

                temp.append(0)

        lst.append(temp)

    return lst


def computeDilation(pixel_array, image_width, image_height):

    lst = copy.deepcopy(pixel_array)

    try:

        for i in range(image_height):

            for j in range(image_width):

                # Top Left Corner

                if i == 0 and j == 0 and (pixel_array[i][j] == 1 or pixel_array[i][j] == 255):

                    lst[i][j] = 1
                    lst[i][j + 1] = 1
                    lst[i + 1][j] = 1
                    lst[i + 1][j + 1] = 1

                # Top Right Corner

                elif i == 0 and j == image_width - 1 and (pixel_array[i][j] == 1 or pixel_array[i][j] == 255):

                    lst[i][j] = 1
                    lst[i][j - 1] = 1
                    lst[i + 1][j] = 1
                    lst[i + 1][j - 1] = 1

                # Bottom Left Corner

                elif i == image_height - 1 and j == 0 and (pixel_array[i][j] == 1 or pixel_array[i][j] == 255):

                    lst[i][j] = 1
                    lst[i][j + 1] = 1
                    lst[i - 1][j] = 1
                    lst[i - 1][j + 1] = 1

                # Bottom Right Corner

                elif i == image_height - 1 and j == 0 and (pixel_array[i][j] == 1 or pixel_array[i][j] == 255):

                    lst[i][j] = 1
                    lst[i][j - 1] = 1
                    lst[i + 1][j] = 1
                    lst[i + 1][j - 1] = 1

                elif (pixel_array[i][j] == 1 or pixel_array[i][j] == 255):

                    lst[i][j] = 1
                    lst[i][j - 1] = 1
                    lst[i][j + 1] = 1

                    lst[i - 1][j] = 1
                    lst[i - 1][j - 1] = 1
                    lst[i - 1][j + 1] = 1

                    lst[i + 1][j] = 1
                    lst[i + 1][j - 1] = 1
                    lst[i + 1][j + 1] = 1

                else:

                    pass

    except IndexError:

        pass

    return lst
