"""
Written by: Enzo Villarama
UPI: evil629

Contents:

This is the main driver code for my QR Scanner/Decoder App
I have chose to write my functions over multiple files in order to separate each function ~ Which for my workflow helps me to debug easier

"""


from matplotlib import pyplot
from matplotlib.patches import Rectangle
from tqdm import tqdm
# from pyzbar.pyzbar import decode

# I wrote my code across several files to separate each function
import convertToGreyscale as ctg
import computeEdges as ce
import imageFiltering as iF
import thresholding
import morphologicalOperations as mO
import connectedComponents as cc

import imageIO.png


# this function reads an RGB color png file and returns width, height, as well as pixel arrays for r,g,b
def readRGBImageToSeparatePixelArrays(input_filename):

    image_reader = imageIO.png.Reader(filename=input_filename)
    # png reader gives us width and height, as well as RGB data in image_rows (a list of rows of RGB triplets)
    (image_width, image_height, rgb_image_rows, rgb_image_info) = image_reader.read()

    print("read image width = {}, height = {}".format(image_width, image_height))

    # our pixel arrays are lists of lists, where each inner list stores one row of greyscale pixels
    pixel_array_r = []
    pixel_array_g = []
    pixel_array_b = []

    for row in rgb_image_rows:
        pixel_row_r = []
        pixel_row_g = []
        pixel_row_b = []
        r = 0
        g = 0
        b = 0
        for elem in range(len(row)):
            # RGB triplets are stored consecutively in image_rows
            if elem % 3 == 0:
                r = row[elem]
            elif elem % 3 == 1:
                g = row[elem]
            else:
                b = row[elem]
                pixel_row_r.append(r)
                pixel_row_g.append(g)
                pixel_row_b.append(b)

        pixel_array_r.append(pixel_row_r)
        pixel_array_g.append(pixel_row_g)
        pixel_array_b.append(pixel_row_b)

    return (image_width, image_height, pixel_array_r, pixel_array_g, pixel_array_b)

# This method packs together three individual pixel arrays for r, g and b values into a single array that is fit for
# use in matplotlib's imshow method


def prepareRGBImageForImshowFromIndividualArrays(r, g, b, w, h):
    rgbImage = []
    for y in range(h):
        row = []
        for x in range(w):
            triple = []
            triple.append(r[y][x])
            triple.append(g[y][x])
            triple.append(b[y][x])
            row.append(triple)
        rgbImage.append(row)

    return rgbImage


def calcBox(r, g, b, w, h):

    # Converts RGB to Greyscale
    image = ctg.computeGreyscale(r, g, b, w, h)

    # Scales Greyscale data to 8bit (0 - 255 bit range)
    image = ctg.scale0to255andQuantize(image, w, h)

    # Determines horizontal and vertical edges
    horizontal = ce.computeHorizontalEdges(image, w, h)
    vertical = ce.computeVerticalEdges(image, w, h)

    # Calculates gradient magnitude
    gradient = ce.computeGradient(horizontal, vertical)

    # Applies Gussian blur
    guassian = iF.guassianFilter(gradient, w, h)

    n = 10  # Number of times you want to apply the guassian filter

    for i in tqdm(range(n)):

        guassian = iF.guassianFilter(guassian, w, h)

    image = ctg.scale0to255andQuantize(guassian, w, h)

    image = thresholding.computeThreshold(image, 70, w, h)

    # Applying Morphological Closing ~ Dialation followed by Erosion
    image = mO.computeDilation(image, w, h)
    image = mO.computeErosion(image, w, h)

    # Label Connected Components ~ Using BFS

    image = cc.connectedComponents(image, w, h)

    dimensions = determineSize(image, w, h)

    return dimensions


def determineSize(image, w, h):

    x, y, width, height = 0, 0, 0, 0

    rows = set()

    columns = set()

    for row in range(h):

        for column in range(w):

            if image[row][column] != 0:

                rows.add(row)
                columns.add(column)

    rows = list(rows)
    columns = list(columns)

    min_y = min(rows)
    max_y = max(rows)

    min_x = min(columns)
    max_x = max(columns)

    print(min_x, max_x, min_y, max_y)

    height = max_y - min_y
    width = max_x - min_x

    x = min_x
    y = min_y

    return [x, y, width, height]


# This method takes a greyscale pixel array and writes it into a png file
def writeGreyscalePixelArraytoPNG(output_filename, pixel_array, image_width, image_height):
    # now write the pixel array as a greyscale png
    file = open(output_filename, 'wb')  # binary mode is important
    writer = imageIO.png.Writer(image_width, image_height, greyscale=True)
    writer.write(file, pixel_array)
    file.close()


def main():
    filename = "./images/covid19QRCode/poster1small.png"

    # we read in the png file, and receive three pixel arrays for red, green and blue components, respectively
    # each pixel array contains 8 bit integer values between 0 and 255 encoding the color values
    (image_width, image_height, px_array_r, px_array_g, px_array_b) = readRGBImageToSeparatePixelArrays(filename)

    pyplot.imshow(prepareRGBImageForImshowFromIndividualArrays(px_array_r, px_array_g, px_array_b, image_width, image_height))

    # Just copied and edited the prepareRGBImageToSeparatePixelArrays
    # pyplot.imshow(calcBox(px_array_r, px_array_g, px_array_b, image_width, image_height), cmap = 'gray')

    dimensions = calcBox(px_array_r, px_array_g, px_array_b, image_width, image_height)

    # get access to the current pyplot figure
    axes = pyplot.gca()
    # create a 70x50 rectangle that starts at location 10,30, 0with a line width of 3

    x = dimensions[0]
    y = dimensions[1]
    width = dimensions[2]
    height = dimensions[3]

    rect = Rectangle((x, y), width, height, linewidth=3, edgecolor='g', facecolor='none')
    # paint the rectangle over the current plot 1
    axes.add_patch(rect)

    # plot the current figure
    pyplot.show()


if __name__ == "__main__":
    main()
