# donut_image_processor.py
from PIL import Image
import numpy as np

def read_image(uploaded_file):
    if uploaded_file is not None:
        return Image.open(uploaded_file)
    else:
        raise FileNotFoundError("No file uploaded")

def process_donut_image(image):
    # Placeholder for actual image processing logic
    # For simplicity, just converting the image to a NumPy array
    return np.array(image)
