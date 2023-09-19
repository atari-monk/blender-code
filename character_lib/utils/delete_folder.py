import shutil


def delete_folder(path):
    try:
        shutil.rmtree(path)
        print(f'Successfully deleted {path}')
    except FileNotFoundError:
        print(f'The folder {path} does not exist.')
    except Exception as e:
        print(f'Error deleting {path}: {e}')
