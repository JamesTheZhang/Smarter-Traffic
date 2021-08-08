import cv2

cap = cv2.VideoCapture('carvideo1.mp4') #use when want to detect objects in a video
#cap = cv2.VideoCapture(0) #use when want to use device camera to detect


car_cascade = cv2.CascadeClassifier('cars.xml')    #use when want to detect cars

#car_cascade = cv2.CascadeClassifier('buses.xml')    #use when want to detect buses

#car_cascade = cv2.CascadeClassifier('eyes.xml')    #use when want to detect eyes


#constantly read each new frame
while True:
    ret, frames = cap.read()
    #makes images easier to read by removing color when detecting images
    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(gray, 1.7, 1)

    for (x ,y ,w ,h) in cars:
        cv2.rectangle(frames ,(x ,y) ,( x +w , y +h) ,(255 ,255 ,0) ,2)

#display each frame with the rectangles drawn onto each detected car
    cv2.imshow('main video', frames)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()


