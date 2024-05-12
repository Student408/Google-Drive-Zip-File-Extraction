from google.colab import drive
drive.mount('/content/drive')

import zipfile
from tqdm import tqdm

# Define a function to extract files from a zip archive with progress tracking
def extract_with_progress(zip_file, extract_path):
    """
    Extracts files from a zip archive to a specified directory with progress tracking.

    Args:
        zip_file (str): Path to the zip file.
        extract_path (str): Path to the directory where files will be extracted.
    """
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        # Get the total number of files in the zip
        total_files = len(zip_ref.infolist())
        
        # Iterate over each file and extract with progress bar
        for file in tqdm(zip_ref.infolist(), desc='Extracting', unit='files', total=total_files):
            zip_ref.extract(file, extract_path)

# Prompt the user to enter the path to the zip file and the extraction directory
print("Please provide the path to the zip file and the extraction directory.")
print("Example zip file path: '/content/drive/My Drive/example_folder/example.zip'")
zip_file_path = input("Enter the path to the zip file: ")

print("Example extraction directory path: '/content/drive/My Drive/example_folder'")
extract_path = input("Enter the path to the extraction directory: ")

# Call the function to extract with progress tracking
extract_with_progress(zip_file_path, extract_path)
