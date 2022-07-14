from heapdict import heapdict
import numpy as np


def findPath(data, start, end, shape):
    # Get number of rows and columns

    imgHeight = shape[0]
    imgColumn = shape[1]

    # Start coordinates
    startRow = start[0]
    StartColumn = start[1]

    # End coordinates
    endRow = end[0]
    endColumn = end[1]

    # Declare arrays. Mark unexplored distances as inf in pursuit of the best path
    # inf = Infinite

    dist = np.array([[float('inf') for x in range(imgColumn)]
                    for y in range(imgHeight)])

    visited = np.array([[False for x in range(imgColumn)]
                       for y in range(imgHeight)])

    prev = {(x, y): 0 for x in range(imgColumn) for y in range(imgHeight)}

    # Provide cardinal directions
    dr = [-1, +1, 0, 0]
    dc = [0, 0, +1, -1]

    # Add priority queue data structure. Use key-value pairs (node index, dist)
    hd = heapdict()

    # Add first node and mark it visisted with no distance weight
    dist[StartColumn, startRow] = 0
    hd[StartColumn, startRow] = 0
    visited[StartColumn, startRow] = True

    reached_end = False

    def visit(r, c):
        for i in range(0, 4):
            rr = r + dr[i]
            cc = c + dc[i]

            if rr < 0 or cc < 0:
                continue
            if rr >= imgHeight or cc >= imgColumn:
                continue
            if visited[rr, cc]:
                continue

            # Save parent node for use in path reconstruction
            node = (r, c)
            prev[rr, cc] = node

            # Keep exploring until the end is reached
            if (rr, cc) == (endColumn, endRow):
                global reached_end
                reached_end = True
                break

            # The core of Dijkstras Algorithm
            d = int(dist[r, c]) + int(data[rr, cc])
            hd[rr, cc] = d
            dist[rr, cc] = d

            visited[rr, cc] = True

    def reconstruct():
        path = []
        xy = (endColumn, endRow)
        path.append(xy)
        while xy != StartColumn:
            if xy == 0:
                break
            path.append(prev[xy])
            xy = prev[xy]
        path.reverse()
        return path

    # MAIN

    while reached_end == False:
        # Tells you which node to visit next based on which key-value pair has the lowest value
        if(len(hd) == 0):
            break
        a = hd.popitem()
        r, c = a[0]
        visit(r, c)

    path = reconstruct()

    return path[1:]
