from collections import Counter


def mergelists(lists):

    lists = sorted([sorted(x) for x in lists])

    resultlist = []

    if len(lists) >= 1:

        resultlist = [lists[0]]

        if len(lists) > 1:

            for lst in lists[1:]:

                listset = set(lst)

                merged = False

                for index in range(len(resultlist)):

                    rset = set(resultlist[index])

                    if len(listset & rset) != 0:

                        resultlist[index] = list(listset | rset)

                        merged = True

                        break

                if not merged:

                    resultlist.append(lst)

    resultlist = [list(set(x)) for x in resultlist]

    return resultlist


def assignlabelsReturnConflicts(pixel_array, image_width, image_height):

    c = 0   # current label

    conflicts = set()

    for i in range(image_height):

        # print(pixel_array[i])

        for j in range(image_width):

            try:

                if i == 0:

                    if pixel_array[i][j] == 1 and pixel_array[i][j - 1] == 0:

                        c += 1

                        pixel_array[i][j] = c

                    elif pixel_array[i][j] == 1 and pixel_array[i][j - 1] >= 1:

                        pixel_array[i][j] = pixel_array[i][j - 1]

                        conflicts.add((pixel_array[i][j], pixel_array[i][j - 1]))

                    elif pixel_array[i][j] == 0:

                        pixel_array[i][j] = 0

                elif j == 0:

                    if pixel_array[i][j] == 1 and pixel_array[i - 1][j] == 0:

                        c += 1

                        pixel_array[i][j] = c

                    elif pixel_array[i][j] == 1 and pixel_array[i - 1][j] >= 1:

                        pixel_array[i][j] = pixel_array[i - 1][j]

                        conflicts.add((pixel_array[i][j], pixel_array[i - 1][j]))

                    elif pixel_array[i][j] == 0:

                        pixel_array[i][j] = 0

                else:

                    if (pixel_array[i][j] == 1 and pixel_array[i][j - 1] >= 1 and pixel_array[i - 1][j] >= 1):

                        pixel_array[i][j] = min(pixel_array[i][j - 1], pixel_array[i - 1][j])

                        conflicts.add((pixel_array[i][j - 1], pixel_array[i - 1][j]))

                    elif (pixel_array[i][j] == 1 and pixel_array[i][j - 1] >= 1):

                        pixel_array[i][j] = pixel_array[i][j - 1]

                    elif (pixel_array[i][j] == 1 and pixel_array[i - 1][j]):

                        pixel_array[i][j] = pixel_array[i - 1][j]

                    elif (pixel_array[i][j] == 1 and (pixel_array[i][j - 1] == 0 and pixel_array[i - 1][j] == 0)):

                        c += 1

                        pixel_array[i][j] = c

                    elif pixel_array[i][j] == 0:

                        pixel_array[i][j] = 0

            except IndexError:

                pass

    return conflicts


def sortlabels(components, pixel_array, image_width, image_height):

    for i in range(image_height):

        for j in range(image_width):

            if pixel_array[i][j] in [x for v in components.values() for x in v]:

                vals = [x for s2 in [sl for sl in components.values() if pixel_array[i][j] in sl] for x in s2]

                for key, value in components.items():

                    if vals == value:

                        pixel_array[i][j] = key

    count = dict(Counter([val for numbers in pixel_array for val in numbers if val != 0]))

    return count


def computeConnectedComponentLabeling(pixel_array, image_width, image_height):

    conflicts = list(assignlabelsReturnConflicts(pixel_array, image_width, image_height))

    conflicts = [list(x) for x in conflicts]

    conflicts = mergelists(conflicts)

    components = dict()

    label = 1

    for i in range(len(conflicts)):

        components[label] = conflicts[i]

        label += 1

    no_components = sortlabels(components, pixel_array, image_width, image_height)

    return (pixel_array, no_components)
