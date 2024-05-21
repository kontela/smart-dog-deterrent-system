import torch
from PIL import Image
import cv2
import numpy as np
import os
import time

# Load your custom YOLO model
model = torch.hub.load('yolov5', 'custom', path='yolov5/runs/train/exp5/weights/best.pt', source='local')

# Define the image directory for saving frames
IMAGE_DIR = "../data/images"
os.makedirs(IMAGE_DIR, exist_ok=True)


def detect_objects(image):
    # Perform detection
    results = model(image)

    # Extract bounding boxes and probabilities
    bounding_boxes = results.xyxy[0].numpy()  # Convert tensor to numpy array
    for box in bounding_boxes:
        x_min, y_min, x_max, y_max, confidence, class_id = box
        class_name = results.names[int(class_id)]
        print(f"Detected {class_name} with confidence {confidence:.2f} at [{x_min}, {y_min}, {x_max}, {y_max}]")

    return results


def detect_and_display(image_path):
    # Fotoğrafı yükle
    image = Image.open(image_path)

    # Nesne tespiti yap
    results = detect_objects(image)

    # Tespit edilen nesneleri ve sınırlayıcı kutuları yazdır
    bounding_boxes = results.xyxy[0].numpy()  # Convert tensor to numpy array
    for box in bounding_boxes:
        x_min, y_min, x_max, y_max, confidence, class_id = box
        class_name = results.names[int(class_id)]
        print(f"Detected {class_name} with confidence {confidence:.2f} at [{x_min}, {y_min}, {x_max}, {y_max}]")

# Fotoğrafın path bilgisini verin
image_path = 'test3.jpeg'
detect_and_display(image_path)



