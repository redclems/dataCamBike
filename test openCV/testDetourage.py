import cv2

# Load the image
image = cv2.imread('velo.jpg')

# Perform object detection (using a pre-trained YOLO model, for example)
# Detect the bike frame and get its bounding box coordinates

# Measure the dimensions of the straight part of the frame (in pixels)

# Define the known length of the reference object (in inches)
known_length = 12  # For example, if the reference object is a 12-inch ruler

# Calculate the calibration factor
calibration_factor = known_length / measured_length_pixels

# Measure the pixel diameter of a wheel
wheel_diameter_pixels = ...

# Estimate the wheel diameter in inches
wheel_diameter_inches = wheel_diameter_pixels * calibration_factor

print(f"Estimated wheel diameter: {wheel_diameter_inches} inches")
