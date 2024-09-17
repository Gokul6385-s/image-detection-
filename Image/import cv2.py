import RPi.GPIO as GPIO

def metal_detection():
    # Example GPIO pin setup
    metal_detector_pin = 17  # Example GPIO pin number
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(metal_detector_pin, GPIO.IN)

    try:
        # Check if metal is detected
        if GPIO.input(metal_detector_pin):
            return True
        else:
            return False
    finally:
        # Ensure GPIO cleanup
        GPIO.cleanup()

# Example usage
if __name__ == "__main__":
    if metal_detection():
        print("Metal detected!")
    else:
        print("No metal detected.")
