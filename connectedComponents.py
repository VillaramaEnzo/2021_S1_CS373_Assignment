import queueClass as Q


# Returns pixel array of only the section thats part of the largest connected component
def returnMax(d, pixel_array, w, h):

    keyofMaxComponent = max(d, key=d.get)

    for i in range(h):

        for j in range(w):

            # If it is not part of the component set pixel value to 0
            # Filters out irrelevant pixels that my hinder our identification proccess
            if pixel_array[i][j] != keyofMaxComponent:

                pixel_array[i][j] = 0


def connectedComponents(pixel_array, w, h):

    label = 1

    dict = {}

    labels = pixel_array

    visited = set()

    q = Q.Queue()

    for row in range(h - 1):

        for column in range(w - 1):

            if pixel_array[row][column] != 0 and (row, column) not in visited:

                dict[label] = 0

                q.enqueue((row, column))
                visited.add((row, column))

                while not q.isEmpty():

                    val = q.dequeue()

                    labels[val[0]][val[1]] = label

                    dict[label] += 1

                    if val[1] > 0:

                        if pixel_array[val[0]][val[1] - 1] != 0 and (val[0], val[1] - 1) not in visited:

                            q.enqueue((val[0], val[1] - 1))

                            visited.add((val[0], val[1] - 1))

                    if val[1] < w - 1:

                        if pixel_array[val[0]][val[1] + 1] != 0 and (val[0], val[1] + 1) not in visited:

                            q.enqueue((val[0], val[1] + 1))
                            visited.add((val[0], val[1] + 1))

                    if val[0] > 0:

                        if pixel_array[val[0] - 1][val[1]] != 0 and (val[0] - 1, val[1]) not in visited:

                            q.enqueue((val[0] - 1, val[1]))
                            visited.add((val[0] - 1, val[1]))

                    if val[0] < h - 1:

                        if pixel_array[val[0] + 1][val[1]] != 0 and (val[0] + 1, val[1]) not in visited:

                            q.enqueue((val[0] + 1, val[1]))
                            visited.add((val[0] + 1, val[1]))

                label += 1

    returnMax(dict, pixel_array, w, h)

    return pixel_array
