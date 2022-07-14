import numpy as np
from pathlib import Path
import time
import dijkstra
import cv2


def findPath(filepath, startX, startY, endX, endY, diagonalAllowed, outputType):
    filename = Path(filepath).name

    img = cv2.imread(filepath, 0)
    img_color = cv2.imread(filepath)

    array = np.asarray(img)

    mat = np.where(array, 1, 1000)

    print("Finding optimal path, please wait...")

    starttime = time.time()

    path = dijkstra.findPath(mat, start=(startX, startY),
                             end=(endX, endY), shape=img.shape)
    endtime = time.time()

    print("Path finding completed")

    print('Time Taken in seconds: ', (endtime-starttime))

    for i in path:
        row = int(i[0])
        column = int(i[1])

        if(outputType == 0):
            img_color[row, column] = (0, 255, 0)
            # uncomment to save the output file
            # cv2.imwrite(filename, img_color)
        elif(outputType == 1):
            img[row, column] = 255
            # uncomment to save the output file
            # cv2.imwrite(filename, img)

    # open the image
    if(outputType == 0):
        cv2.imshow("Image", img_color)
    elif(outputType == 1):
        cv2.imshow("Image", img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
