import cv2

# Replace the below URL with the URL shown on your IP Webcam app
url = 'http://192.168.1.3:8080/video'

# Use OpenCV to capture the video stream
cap = cv2.VideoCapture(url)

while True:
    ret, frame = cap.read()
    if ret:
        # Display the frame
        cv2.imshow('Video Stream', frame)

        # Press 'q' to close the window
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
