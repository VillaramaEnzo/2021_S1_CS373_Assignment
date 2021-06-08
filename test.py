import connectedComponents as cc

image_width = 16
image_height = 16
pixel_array = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

(ccimg, ccsizes) = cc.computeConnectedComponentLabeling(pixel_array, image_width, image_height)

for i in range(len(ccimg)):
    print(ccimg[i])

print("label: nr_pixels")

for sz in ccsizes.keys():
    print("{}: {}".format(sz, ccsizes[sz]))

print()


image_width = 6
image_height = 6
pixel_array = [
        [1, 1, 0, 1, 1, 0],
        [1, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 1, 1],
        [0, 0, 0, 1, 1, 0],
        [1, 0, 0, 0, 1, 0],
        [1, 0, 1, 1, 1, 0],
        ]

(ccimg, ccsizes) = cc.computeConnectedComponentLabeling(pixel_array, image_width, image_height)

for i in range(len(ccimg)):
    print(ccimg[i])

print("label: nr_pixels")

for sz in ccsizes.keys():
    print("{}: {}".format(sz, ccsizes[sz]))
