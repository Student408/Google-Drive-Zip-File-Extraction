# Google Drive Zip File Extraction using Colab

Fastest way to extract the Zip file. 

This Python script enables you to extract files from a zip archive stored in Google Drive using Google Colab. It incorporates progress tracking to monitor the extraction process, which is particularly beneficial for large zip files.

## Prerequisites

- Python 3.x
- tqdm library

## Usage

1. **Mount Google Drive**: Before executing the script, mount your Google Drive by running the following command and following the prompts:

   ```python
   from google.colab import drive
   drive.mount('/content/drive')
   ```

2. **Run the Script**: Execute the script by running:

   ```bash
   python extract_zip.py
   ```

   Ensure to replace `extract_zip.py` with the actual filename where you've saved the extraction script.

## Customization

You can customize the script by modifying the following variables:

- `zip_file_path`: Path to the zip file you want to extract.
- `extract_path`: Path to the directory where files will be extracted.

## Example

```python
# Path to the zip file and the extraction directory
zip_file_path = '/content/drive/My Drive/example_folder/example.zip'
extract_path = '/content/drive/My Drive/example_folder'

# Call the function to extract with progress tracking
extract_with_progress(zip_file_path, extract_path)
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any improvements or bug fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
