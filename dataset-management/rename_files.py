import os
import re

def rename_files(folder_path, mode, **kwargs):
    """
    Comprehensive file renaming script.

    Args:
        folder_path (str): Path to the folder containing files to rename.
        mode (str): Renaming mode. Options are:
            - "add_prefix": Add a prefix to filenames.
            - "add_suffix": Add a suffix to filenames.
            - "remove_prefix": Remove a specific prefix from filenames.
            - "remove_suffix": Remove a specific suffix from filenames.
            - "change_extension": Change file extensions.
            - "replace_text": Replace a specific text pattern in filenames.
            - "number_files": Rename files with sequential numbers.
        kwargs (dict): Additional arguments required for specific modes.
    """
    # Check if folder exists
    if not os.path.isdir(folder_path):
        print(f"Error: The folder '{folder_path}' does not exist.")
        return

    # Loop through all files in the specified folder
    for idx, filename in enumerate(os.listdir(folder_path)):
        # Skip directories
        if os.path.isdir(os.path.join(folder_path, filename)):
            continue

        # Generate new filename based on the mode
        new_name = filename

        if mode == "add_prefix":
            prefix = kwargs.get("prefix", "")
            new_name = prefix + filename

        elif mode == "add_suffix":
            suffix = kwargs.get("suffix", "")
            name, ext = os.path.splitext(filename)
            new_name = name + suffix + ext

        elif mode == "remove_prefix":
            prefix = kwargs.get("prefix", "")
            if filename.startswith(prefix):
                new_name = filename[len(prefix):]

        elif mode == "remove_suffix":
            suffix = kwargs.get("suffix", "")
            if filename.endswith(suffix):
                new_name = filename[:-len(suffix)]

        elif mode == "change_extension":
            new_extension = kwargs.get("new_extension", "")
            name, _ = os.path.splitext(filename)
            new_name = name + new_extension

        elif mode == "replace_text":
            old_text = kwargs.get("old_text", "")
            new_text = kwargs.get("new_text", "")
            new_name = re.sub(re.escape(old_text), new_text, filename)

        elif mode == "number_files":
            prefix = kwargs.get("prefix", "")
            suffix = kwargs.get("suffix", "")
            ext = os.path.splitext(filename)[1]
            new_name = f"{prefix}{idx + 1:03}{suffix}{ext}"

        else:
            print(f"Error: Unsupported mode '{mode}'.")
            return

        # Full path to the old and new file names
        old_file = os.path.join(folder_path, filename)
        new_file = os.path.join(folder_path, new_name)

        # Rename the file if the name has changed
        if old_file != new_file:
            os.rename(old_file, new_file)
            print(f"Renamed: {filename} -> {new_name}")

    print("Renaming completed.")

# Example Usage:

# Specify the folder path where the files are located
folder_path = "results_2024-10-30"

# Call the function with desired mode and parameters
rename_files(folder_path, mode="add_prefix", prefix="NEW_")
rename_files(folder_path, mode="remove_prefix", prefix="OLD_")
rename_files(folder_path, mode="change_extension", new_extension=".txt")
rename_files(folder_path, mode="replace_text", old_text="draft", new_text="final")
rename_files(folder_path, mode="number_files", prefix="file_", suffix="_processed")
