import zipfile
import os


def zip_folder(folder_to_zip, output_zip_file):
    """
    Zip the contents of a folder into a zip file.

    Args:
        folder_to_zip (str): The path to the folder you want to zip.
        output_zip_file (str): The path for the output zip file.
    """
    try:
        with zipfile.ZipFile(output_zip_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, _, files in os.walk(folder_to_zip):
                for file in files:
                    relative_path = os.path.relpath(
                        os.path.join(root, file), folder_to_zip)
                    zipf.write(os.path.join(root, file), relative_path)
        print(f'Successfully zipped {folder_to_zip} to {output_zip_file}')
    except Exception as e:
        print(f'Error zipping {folder_to_zip}: {e}')
