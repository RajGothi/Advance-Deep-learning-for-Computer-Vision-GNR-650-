import os
import pandas as pd
from sklearn.model_selection import train_test_split
from torchvision.transforms import transforms

from PIL import Image

def crop_center(image, new_width, new_height):
    """
    Crop the center portion of a given image to the specified dimensions.
    :param image: PIL image
    :param new_width: New width of the cropped region
    :param new_height: New height of the cropped region
    :return: Cropped PIL image
    """
    width, height = image.size

    # Calculate the coordinates of the center region
    left = (width - new_width) // 2
    top = (height - new_height) // 2
    right = left + new_width
    bottom = top + new_height

    # Crop the center of the image
    cropped_image = image.crop((left, top, right, bottom))

    return cropped_image

def get_nine_crops(image):
    """
    Divide a square PIL image into nine equal-sized crops.
    :param image: PIL image (assumes height and width are the same)
    :return: List of nine PIL image crops
    """
    width, height = image.size
    crop_size = width // 3  # Calculate the size of each crop

    r_values = [0, crop_size, 2 * crop_size]  # Row starting positions
    c_values = [0, crop_size, 2 * crop_size]  # Column starting positions

    cropped_patches = []

    for r in r_values:
        for c in c_values:
            # Calculate the coordinates for each crop
            left = c
            top = r
            right = c + crop_size
            bottom = r + crop_size

            # Crop and append each region to the list
            patch = image.crop((left, top, right, bottom))
            cropped_patches.append(patch)

    return cropped_patches

def get_paths():
    data_dir = 'CIFAR-10-images/train'
    file_paths_to_return = []
    
    for root, dirs, files in os.walk(data_dir):
        for file in files:
            if file.endswith(".jpg"):
                file_paths_to_return.append(root+'/'+file)                        
    
    return file_paths_to_return

