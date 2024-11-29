import os

def find_python_files_with_code(base_path, target_line):
    matching_files = []

    # Walk through the directory and subdirectories
    for root, _, files in os.walk(base_path):
        for file in files:
            if file.endswith('.py'):  # Check for Python files
                file_path = os.path.join(root, file)
                try:
                    # Open and read the file
                    with open(file_path, 'r', encoding='utf-8') as f:
                        for line in f:
                            if target_line in line:  # Check for the target line
                                matching_files.append(file_path)
                                break
                except (UnicodeDecodeError, IOError):  # Handle read errors
                    print(f"Could not read file: {file_path}")

    return matching_files


if __name__ == "__main__":
    # Specify the base directory to start searching (e.g., your home directory)
    base_directory = os.path.expanduser("~")  # Your home directory
    target_code_line = "if num_inliers < min_inliers:"

    print("Searching for .py files containing the target line...")
    result_files = find_python_files_with_code(base_directory, target_code_line)

    if result_files:
        print("\nFiles containing the target line:")
        for file in result_files:
            print(file)
    else:
        print("\nNo matching files found.")
