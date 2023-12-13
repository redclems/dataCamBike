# main.py
import cv2
import image_processing
import numpy as np

def normalize_image(image):
    if image is not None:
        # Convert image to float32 to perform arithmetic operations
        image = image.astype(np.float32)

        # Normalize the image to the range [0, 1]
        normalized_image = cv2.normalize(image, None, 0.0, 1.0, cv2.NORM_MINMAX)

        return normalized_image
    else:
        return None

def resize_and_convert_to_bw(image):
    if image is not None:
        resized_image = cv2.resize(image, (500, 500))
        grayscale_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
        return grayscale_image
    else:
        return None

