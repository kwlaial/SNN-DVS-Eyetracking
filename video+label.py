import cv2 as cv
import numpy as np

data = np.load("C:/Users/85261/OneDrive - HKUST Connect/others/documents/SNN-DVS-Eyetracking/dataset.npy")
label = np.load("C:/Users/85261/OneDrive - HKUST Connect/others/documents/SNN-DVS-Eyetracking/label.npy")

for index, frame in enumerate(data):

    cv.circle(frame, (label[index][0], label[index][1]), 30, 180, 10)
    cv.imshow('frame', frame)
    if cv.waitKey(1) == ord('q'):
        break

cv.destroyAllWindows()