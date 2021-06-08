def computeThreshold(pixel_array, threshold_value, image_width, image_height):

    for i in range(image_height):

        for j in range(image_width):

            if pixel_array[i][j] >= threshold_value:

                pixel_array[i][j] = 255

            else:

                pixel_array[i][j] = 0

    return pixel_array
