import cv2


ss=cv2.VideoCapture(0)
source=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter("Record.avi",source,20.0,(1080,740))
while True:
    video,frame=ss.read()
    cv2.imshow("Video",frame)
    cv2.imshow("2Video",frame)
    if cv2.waitKey(1)==ord('q'):
        break
ss.release()
