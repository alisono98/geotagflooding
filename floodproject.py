# -*- coding: utf-8 -*-
"""floodproject.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1XLEyC-prrhEb8hLUH2yXMP8Qj9d-0FpJ
"""

!pip install fiftyone

# LOADAS IMAGE DIRECTORY
import zipfile
import os

# Replace 'your_file.zip' with the name of your uploaded file
zip_file_name = '/content/archive.zip'

# Create a directory to extract files (optional)
extraction_path = './Dataset/images'
os.makedirs(extraction_path, exist_ok=True)

# Unzip the file
with zipfile.ZipFile(zip_file_name, 'r') as zip_ref:
    zip_ref.extractall(extraction_path)

print("Files extracted to:", extraction_path)

# for sample in dataset:
#   img_filepath = 'sample.filepath'
#   LOGIC TO GET ANNOTATION FILEPATH
#   sample["Segmentation"] = fo.Segmentation(mask_path=mask_path)
#   sample.save()

import fiftyone as fo

name = "seg"
dataset_dir = "/content/Dataset/images/Dataset/data"

# Create the dataset
dataset = fo.Dataset.from_dir(
    dataset_dir=dataset_dir,
    dataset_type=fo.types.ImageDirectory,
    name=name,
    overwrite=True
)

# View summary info about the dataset
print(dataset)

# Print the first few samples in the dataset
print(dataset.head())

for sample in dataset.iter_samples(progress=True, autosave=True):
    fp = sample.filepath
    print(fp)
    file_num = fp.split("_")[1].split(".")[0]
    mask_path = f"/content/Dataset/images/Dataset/labels/label_{file_num}.png"
    sample["Segmentation"] = fo.Segmentation(mask_path=mask_path)

session = fo.launch_app(dataset)

# Load your dataset
dataset = fo.load_dataset("seg")

# Iterate through each sample in the dataset
for sample in dataset:
    print(sample)
    # Access the segmentation data
    segmentation = sample.Segmentation  # Adjust the field name as necessary
    label = segmentation.id

        # Perform your analysis or processing here
    print(f"Label: {label}")

for sample in dataset.iter_samples(progress=True, autosave=True):
    fp = sample.filepath
    print(fp)
    file_num = fp.split("_")[1].split(".")[0]
    mask_path = f"/content/Dataset/images/Dataset/labels/label_{file_num}.png"

    # Check if segmentation ID exists (assuming "Segmentation" field indicates this)
    if "Segmentation" in sample and sample["Segmentation"] is not None and sample["Segmentation"].mask_path is not None:
        # Create 'flooded' object (using Detections for consistency with previous example)
        sample["Segmentation"] = fo.Segmentation(mask_path=mask_path)
        # ... (rest of the code to define the 'flooded' object as before) ...

    else:
        # Create 'no flood' object
        sample["detections"] = fo.Detections(detections=[
            fo.Detection(
                label="no flood",
                # ... (optional: add bounding box or other properties for 'no flood') ...
            )
        ])

from PIL import Image
import numpy as np

im = Image.open("/content/Dataset/images/Dataset/images/image_1.jpg")

im

