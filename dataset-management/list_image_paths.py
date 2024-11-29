import os

# Set the source folder path
source_folder = r'C:\Users\RoscoeKerby\Downloads\OneDrive_2024-10-17\01_Bostu Boerboele'

# Function to list all image paths in a folder and its subfolders
def list_images_in_folder_recursive(folder_path):
    image_extensions = ('.jpg', '.jpeg', '.png', '.JPG', '.JPEG', '.PNG')  # Case-insensitive image extensions
    image_paths = []
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(image_extensions):  # Ensure case-insensitive comparison
                image_paths.append(os.path.join(root, file))
    return image_paths

# Get the list of all image paths
all_image_paths = list_images_in_folder_recursive(source_folder)

# Print each image path
for image_path in all_image_paths:
    print(image_path)

print(str(len(all_image_paths)))

# Optionally, return the list of image paths
# If you want to use the list elsewhere in your code:
# return all_image_paths
