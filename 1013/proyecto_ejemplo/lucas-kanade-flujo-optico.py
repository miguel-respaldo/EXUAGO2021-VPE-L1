import numpy as np
import cv2 as cv

# Use camera for capture
cap = cv.VideoCapture(0)

# Create params for ShiTomasi corner detection
feature_params = dict(maxCorners=100,
                      qualityLevel=0.3,
                      minDistance=7,
                      blockSize=7)

# Create params for lucas kanade optical flow
lk_params = dict(winSize=(15, 15),
                 maxLevel=2,
                 criteria=(cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT,
                           10, 0.03))

# Create some random colors
color = np.random.randint(0, 255, (100, 3))

# Take first frame and find corners in it
_, old_frame = cap.read()
old_gray = cv.cvtColor(old_frame, cv.COLOR_BGR2GRAY)
p0 = cv.goodFeaturesToTrack(old_gray, mask=None, **feature_params)

# Create a mask image for drawing purposes
mask = np.zeros_like(old_frame)

while True:

    # Capture a frame
    _, frame = cap.read()

    # Convert it to grayscale
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Calculate optical flow
    p1, st, err = cv.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None,
                                          **lk_params)

    # If no flow, look for new points
    if p1 is None:

        old_gray = cv.cvtColor(old_frame, cv.COLOR_BGR2GRAY)

        p0 = cv.goodFeaturesToTrack(old_gray, mask=None, **feature_params)

        # Get rid of old lines
        mask = np.zeros_like(old_frame)

        cv.imshow('frame', frame)

    # Otherwise, show flow
    else:

        # Select good points
        good_new = p1[st == 1]
        good_old = p0[st == 1]

        # Draw the tracks
        for i, (new, old) in enumerate(zip(good_new, good_old)):
            a, b = (int(x) for x in new.ravel())
            c, d = (int(x) for x in old.ravel())
            mask = cv.line(mask, (a, b), (c, d), color[i].tolist(), 2)
            frame = cv.circle(frame, (a, b), 5, color[i].tolist(), -1)

        # Display the image with the flow lines
        img = cv.add(frame, mask)
        cv.imshow('frame', img)

        # Update the previous frame and previous points
        old_gray = frame_gray.copy()
        p0 = good_new.reshape(-1, 1, 2)

    # Force display, quitting on ESC
    if (cv.waitKey(1) & 0xff) == 27:
        break

# Shut down
cv.destroyAllWindows()
cap.release()