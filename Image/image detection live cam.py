import cv2

# Load the pre-trained face detection model
facedetect = cv2.CascadeClassifier(r"C:\Users\gokul\Downloads\haarcascade_frontalface_alt.xml")

# Capture video from the webcam
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the webcam
    ret, img = cap.read()
    
    # Convert the frame to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the grayscale frame
    faces = facedetect.detectMultiScale(gray, 1.1, 4)
    
    # Draw rectangles around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    
    # Display the frame with rectangles drawn
    cv2.imshow('img', img)
    
    # Wait for the 'Esc' key to be pressed to exit
    k = cv2.waitKey(30) & 0xff
    if k == 27:  # ASCII for 'Esc'
        break

# Release the webcam and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
