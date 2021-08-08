import cv2
import numpy as np
from time import sleep

width_min = 80  # width minimum of the rectangle in pixels
height_min = 80  # Minimum height of the rectangle in pixels

offset = 6  # Allowable error between pixels

pos_line = 550  # Count Line Position

delay = 60  # Video FPS

detect = []
cars = 0
buses = 0

#find center of car/truck
def catch_center(x, y, w, h):
    x1 = int(w / 2)
    y1 = int(h / 2)
    cx = x + x1
    cy = y + y1
    return cx, cy


cap = cv2.VideoCapture('video.mp4')
#isolates vehicles and removes(subtracts) the background
subtraction = cv2.createBackgroundSubtractorKNN()

while True:
    #waits every frame to repeat
    ret, frame1 = cap.read()
    tempo = float(1 / delay)
    sleep(tempo)

    #change video feed to grey so its easier for the program to recognize objects
    grey = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    #smoothen the video feed of sharp edges
    blur = cv2.GaussianBlur(grey, (3, 3), 5)
    img_sub = subtraction.apply(blur)

    #make vehicles larger and easier to recognize by the program
    dilate = cv2.dilate(img_sub, np.ones((5, 5)))
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    dilated = cv2.morphologyEx(dilate, cv2.MORPH_CLOSE, kernel)
    dilated = cv2.morphologyEx(dilated, cv2.MORPH_CLOSE, kernel)
    #draws an imaginary line indicating the border of the vehicle detected after bloating done above
    contour, h = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    #draws a detection line(if detected cars pass though here then counter goes up)
    cv2.line(frame1, (25, pos_line), (1200, pos_line), (255, 127, 0), 3)
    #draws a rectangle around the vehicle detected earlier
    for (i, c) in enumerate(contour):
        (x, y, w, h) = cv2.boundingRect(c)
        validate_contour = (w >= width_min) and (h >= height_min)
        if not validate_contour:
            continue
        #gives the rectangle a color and gives its center a color
        cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
        center = catch_center(x, y, w, h)
        detect.append(center)
        cv2.circle(frame1, center, 4, (0, 0, 255), -1)

        for (x, y) in detect:
            if y < (pos_line + offset) and y > (pos_line - offset):
                cars += 1
                cv2.line(frame1, (25, pos_line), (1200, pos_line), (0, 127, 255), 3)
                detect.remove((x, y))
                print("car is detected : " + str(cars))
                f = open('C:\\XDHacks\\src\\xdhacks\\traffic.txt', mode='wt', encoding='utf-8')
                f.write(str(cars)+"\n" + str(buses))
                f.close()

    cv2.putText(frame1, "VEHICLE COUNT : " + str(cars), (450, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 3)
    cv2.imshow("Video Original", frame1)
    # cv2.imshow("Detectar",dilated)

    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()
