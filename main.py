# a file for getting video from camera and processing it
import cv2
import numpy as np
import serial
import time

# Change 'COM3' to the serial port your Arduino is connected to
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
# Create a VideoCapture object
cap = cv2.VideoCapture(2)
blue_lego = False
time.sleep(2)  # wait for the serial connection and the camera to initialize
# Check if the camera is opened
if not cap.isOpened():
    print("Cannot open camera")
    exit()
elif not ser.is_open:
    print("Cannot open serial")
    exit()
else: 
    print("Camera is opened")
    # show the video
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        # Our operations on the frame come here
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # now, set the lower and upper HSV limits to detect the color
        lower_blue = np.array([100, 100, 50])
        upper_blue = np.array([130, 255, 255])
        # Threshold the HSV image to get only blue colors
        mask = cv2.inRange(hsv, lower_blue, upper_blue)
        # get the percentage of the blue color in the frame
        percentage = (np.sum(mask == 255) / mask.size) * 100
        # clear the console
        print("\033c", end="")
        print('Percentage of blue color in the frame: ', percentage, '%')
        if percentage > 1:
            print('Blue Lego!')
            if not blue_lego:
                blue_lego = True
                ser.write('1'.encode())  # Tell the Arduino that the blue lego is detected
        else:
            print('No Blue Lego!')
            if blue_lego:
                blue_lego = False
                ser.write('0'.encode()) # Tell the Arduino that the blue lego is not detected
        # show the mask
        cv2.imshow('mask', mask)
        if cv2.waitKey(1) == ord('q'):
            break