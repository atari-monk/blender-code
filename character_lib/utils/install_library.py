import sys
import zipfile
import os
from delete_folder import delete_folder
from ziper import zip_folder


folder_to_zip = 'C:/atari-monk/Code/blender-code/character_lib'
output_zip_file = 'C:/atari-monk/Code/blender-code/character_lib.zip'
zip_folder(folder_to_zip, output_zip_file)

library_extraction_dir = 'C:/Users/ASUS/AppData/Roaming/Blender Foundation/Blender/3.6/scripts/modules/character_lib'

delete_folder(library_extraction_dir)

with zipfile.ZipFile(output_zip_file, 'r') as zip_ref:
    zip_ref.extractall(library_extraction_dir)

library_path = os.path.join(library_extraction_dir, 'character_lib')
if library_path not in sys.path:
    sys.path.append(library_path)

try:
    os.remove(output_zip_file)
    print(f'Successfully deleted {output_zip_file}')
except FileNotFoundError:
    print(f'The file {output_zip_file} does not exist.')
except Exception as e:
    print(f'Error deleting {output_zip_file}: {e}')
