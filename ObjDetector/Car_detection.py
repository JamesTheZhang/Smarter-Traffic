import cv2

cap = cv2.VideoCapture('carvideo1.mp4')
car_cascade = cv2.CascadeClassifier('cars.xml')

car_count1 = 0
bus_count1 = 0

#constantly read each new frame
while True:
    ret, frames = cap.read()
    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(gray, 1.7, 1)

    for (x ,y ,w ,h) in cars:
        cv2.rectangle(frames ,(x ,y) ,( x +w , y +h) ,(255 ,255 ,0) ,2)

#display each frame with the rectangles drawn onto each detected car
    cv2.imshow('main video', frames)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()

f=open('C:\\XDHacks\\src\\xdhacks\\traffic.txt', mode='wt', encoding='utf-8' )
f.write(str(car_count1)+"\n" + str(bus_count1))
f.close()

