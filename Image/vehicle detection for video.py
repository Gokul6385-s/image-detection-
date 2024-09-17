import cv2

# Load the car cascade (replace with the correct XML file for car detection)
cars_cascade = cv2.CascadeClassifier(r"C:\Users\gokul\Downloads\cars.xml")

# Function to detect cars
def detect_cars(frame):
    # Detect cars in the frame
    cars = cars_cascade.detectMultiScale(frame, 1.1, 1)
    for (x, y, w, h) in cars:
        # Draw rectangles around detected cars
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 4)
    return frame

# Function to simulate the car detection in a video
def simulator():
    # Load the video
    car_video = cv2.VideoCapture(r"C:/Users/gokul/Downloads/mixkit-two-avenues-with-many-cars-traveling-at-night-34562-hd-ready.mp4")
    
    while car_video.isOpened():
        ret, frame = car_video.read()
        controlkey = cv2.waitKey(1)
        
        if ret:
            # Detect cars and display the frame
            cars_frame = detect_cars(frame)
            cv2.imshow('Car Detection', cars_frame)
        else:
            break
        
        # Press 'q' to exit
        if controlkey == ord('q'):
            break
    
    # Release the video capture object and close windows
    car_video.release()
    cv2.destroyAllWindows()

# Run the simulator
simulator()
