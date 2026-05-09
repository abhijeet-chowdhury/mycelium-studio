from pathlib import Path

# Specify the directory path
folder_path = Path('/Users/abhijeet/Desktop/portfolio/ images')

# Check if the path exists and is a directory
if folder_path.is_dir():
    # Iterate over all items in the directory
    for file in folder_path.iterdir():
        # Filter to ensure we only print files (ignoring subfolders)
        if file.is_file():
            print(file.name)
else:
    print("The specified path does not exist or is not a directory.")