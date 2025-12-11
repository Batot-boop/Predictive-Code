import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os
import sys

def get_image_path():
    # Prompts user for image path.
    while True:
        path = input("Enter the full path to the image: ").strip()
        if os.path.exists(path):
            return path
        print("File not found. Please try again.")

def load_image(path):
    try:
        img = Image.open(path).convert('L')
        # Using float64 for prevent math errors
        return np.array(img, dtype=np.float64) 
    except Exception as e:
        print(f"Error loading image: {e}")
        return None

def predictor_2d():
    img = load_image(get_image_path())
    h, w = img.shape
    predictor = np.zeros((h, w), dtype=np.float64)
    for x in range(h): # rows
        for y in range(w): # columns
            
            left = img(x, y-1) if x > 0 else 0
            up = img(x-1, y) if y > 0 else 0
            
            if x == 0 and y == 0:
                guess = 0
            elif x == 0:
                guess = up
            elif y == 0:
                guess = left
            else:
                guess = (left + up) / 2
            predictor(x, y) = guess

    error_matrix = img - predictor
    return predictor, error_matrix
    

def uniform_quantizer():
    pass

def reconsturcted_image():
    pass

def main():
    pass

if __name__ == "__main__":
    main()