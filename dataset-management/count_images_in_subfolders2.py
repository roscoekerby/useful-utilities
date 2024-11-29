import os

# Set the source folder path
source_folder = r'C:\Users\RoscoeKerby\Downloads\OneDrive_2024-10-17\01_Bostu Boerboele'


# Function to list all image paths in a folder and its subfolders, and count per folder
def list_images_and_count_by_folder(folder_path):
    image_extensions = ('.jpg', '.jpeg', '.png', '.JPG', '.JPEG', '.PNG')  # Case-insensitive image extensions
    image_paths = []
    folder_image_count = {}

    # Walk through all directories and subdirectories
    for root, dirs, files in os.walk(folder_path):
        # Set the folder name from the root
        folder_name = os.path.relpath(root, folder_path)  # Relative path to the folder
        folder_image_count[folder_name] = 0  # Initialize count for this folder

        for file in files:
            # Check if the file is an image
            if file.lower().endswith(image_extensions):
                # Add the image path to the list
                full_path = os.path.join(root, file)
                image_paths.append(full_path)
                # Increment count for this folder
                folder_image_count[folder_name] += 1

    return image_paths, folder_image_count


# Get the list of all image paths and the image count per folder
all_image_paths, image_count_per_folder = list_images_and_count_by_folder(source_folder)

# Print each image path
for image_path in all_image_paths:
    print(image_path)

# Print the number of images in each folder
for folder, count in image_count_per_folder.items():
    print(f"{folder}: {count} images")

# Print the total number of images
print(f"Total images: {len(all_image_paths)}")
