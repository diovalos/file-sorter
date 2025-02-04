import os
import re
from collections import defaultdict

# Directory containing the videos
source_directory = r"C:\Users\Earth\AppData\Local\Packages\38833FF26BA1D.UnigramPreview_g9c9v27vpyspw\LocalState\0\videos"

# Destination directory for sorted folders
destination_directory = r"C:\Users\Earth\AppData\Local\Packages\38833FF26BA1D.UnigramPreview_g9c9v27vpyspw\LocalState\0\videos"

# Create destination directory if it doesn't exist
os.makedirs(destination_directory, exist_ok=True)

# Function to extract numeric part from file name
def extract_number(filename):
    match = re.search(r"\d+", filename)
    return int(match.group()) if match else None


# Group files by serial number
files = [f for f in os.listdir(source_directory) if f.lower().endswith(('.mp4', '.jpg', '.png'))]
serial_groups = defaultdict(list)

for file in files:
    serial_number = extract_number(file)
    if serial_number is not None:
        serial_groups[serial_number // 10].append((serial_number, file))

# Sort and organize files into folders
for group, items in serial_groups.items():
    items.sort()  # Sort by serial number
    folder_name = str(items[0][0])  # Use first file's serial as folder name
    folder_path = os.path.join(destination_directory, folder_name)
    os.makedirs(folder_path, exist_ok=True)

    for _, file in items:
        source_path = os.path.join(source_directory, file)
        destination_path = os.path.join(folder_path, file)
        os.rename(source_path, destination_path)

print("Videos sorted successfully.")
