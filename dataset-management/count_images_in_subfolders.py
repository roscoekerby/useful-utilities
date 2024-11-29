import os

# Set the source folder path
source_folder = r'C:\Users\RoscoeKerby\Downloads\OneDrive_2024-10-17\01_Bostu Boerboele'


# Function to count images in a folder and its subfolders
def count_images_in_folder_recursive(folder_path):
    image_extensions = ('.jpg', '.jpeg', '.png', '.JPG', '.JPEG', '.PNG')  # Case-insensitive image extensions
    image_count = 0
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(image_extensions):  # Ensure case-insensitive comparison
                image_count += 1
    return image_count


# Dictionary to store the count of images per folder
folder_image_counts = {}

# Walk through all directories and subdirectories in the source folder
total_images = 0
for root, dirs, files in os.walk(source_folder):
    # Count the number of images in this folder and all its subfolders
    total_images_in_folder = count_images_in_folder_recursive(root)

    # Store the count in the dictionary using the folder name
    folder_name = os.path.basename(root) if os.path.basename(root) else 'root'
    folder_image_counts[folder_name] = total_images_in_folder

    # Add to the total image count
    total_images += total_images_in_folder

# Print the image count per folder and its subfolders
for folder, total_count in folder_image_counts.items():
    print(f"{folder}: {total_count} images (including subfolders)")

# Print the total image count
print(f"Total images in root and all subfolders: {total_images}")
