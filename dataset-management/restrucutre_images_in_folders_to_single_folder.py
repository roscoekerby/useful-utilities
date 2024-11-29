import os
import shutil

# Set source and destination folder paths
source_folder = r'C:\Users\RoscoeKerby\Downloads\OneDrive_2024-10-17'
destination_folder = r'C:\Users\RoscoeKerby\Downloads\OneDrive_2024-10-17\BostonDogs'

# Create the destination folder if it does not exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Function to handle duplicate file names by appending _copy<I> if necessary
def get_unique_filename(destination_path):
    filename, file_extension = os.path.splitext(destination_path)
    counter = 1
    while os.path.exists(destination_path):
        destination_path = f"{filename}_copy{counter}{file_extension}"
        counter += 1
    return destination_path

# Walk through all directories and subdirectories in the source folder
for root, dirs, files in os.walk(source_folder):
    for file in files:
        # Check if the file is an image (jpg, jpeg, png)
        if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png"):
            # Construct full file paths for source and destination
            source_file = os.path.join(root, file)
            destination_file = os.path.join(destination_folder, file)

            # Get a unique filename if there is a conflict
            destination_file = get_unique_filename(destination_file)

            # Copy the file
            shutil.copy(source_file, destination_file)
            print(f"Copied: {file} from {root} to {destination_file}")

print("All image files from subfolders have been copied successfully.")