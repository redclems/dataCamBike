import cv2
import numpy as np
from picamera import PiCamera

# Initialize the PiCamera
camera = PiCamera()

# Capture an image in memory (no need to save it to disk)
image_stream = io.BytesIO()
camera.capture(image_stream, format="jpeg")
image_data = np.frombuffer(image_stream.getvalue(), dtype=np.uint8)
image = cv2.imdecode(image_data, cv2.IMREAD_COLOR)

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to reduce noise
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Apply adaptive thresholding to create a binary image
_, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Find contours in the binary image
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Filter contours based on size or other criteria
filtered_contours = [contour for contour in contours if cv2.contourArea(contour) > 1000]

# Create a black mask for the segmented bike
mask = np.zeros_like(gray)

# Draw the filtered contours on the mask
cv2.drawContours(mask, filtered_contours, -1, 255, thickness=cv2.FILLED)

# Bitwise AND to extract the segmented bike
segmented_bike = cv2.bitwise_and(image, image, mask=mask)

# Save or process the segmented bike image for later analysis
cv2.imwrite("segmented_bike.jpg", segmented_bike)

# Display the segmented bike
cv2.imshow("Segmented Bike", segmented_bike)
cv2.waitKey(0)
cv2.destroyAllWindows()
