from textnode import *

import os
import shutil

source_dir = r"./static"
dest_dir = r"./public"

def delete_dir_contents(path):
    contents = os.listdir(path)
    for item in contents:
        item_path = os.path.join(path, item)
        if os.path.isfile(item_path):
            removed_path = os.remove(item_path)
            print('File deleted at: ', removed_path)
        else:
            removed_dir = shutil.rmtree(item_path)
            print('Directory tree removed at: ', removed_dir)


def copy_contents_recursive(source_dir, dest_dir):
    # Ensure dest_dir exists
    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)

    for item in os.listdir(source_dir):
        source_path = os.path.join(source_dir, item)
        dest_path = os.path.join(dest_dir, item)

        if os.path.isfile(source_path):
            shutil.copy(source_path, dest_path)
            print(f"   Copied {source_path} to {dest_path}")
        else:
            copy_contents_recursive(source_path, dest_path)


# Write a *recursive* function that copies all the contents
# from a 'static' directory to a 'public' directory
# (without using 'shutil.copytree')
def copy_dir(source_dir, dest_dir):
    # Ensure path arguments exist
    if os.path.exists(source_dir):
        source_path = os.path.join(source_dir)
        print("source path: ", source_path)
    else:
        raise ValueError("Source path does not exist.")
    
    if os.path.exists(dest_dir):
        dest_path = os.path.join(dest_dir)
        print("destination path: ", dest_path)
    else:
        raise ValueError("Destination path does not exist.")
    
    print("-----")

    # Delete destination dir contents
    try:
        delete_dir_contents(dest_dir)
        print('Destination directory contents deleted successfully.')
    except:
        raise Exception('Failed to delete destination directory.')
    
    print("-----")

    try:
        copy_contents_recursive(source_path, dest_path)
        print("Successfully copied contents")
    except:
        raise Exception("Failed to copy contents")
    

def main():
    copy_dir(source_dir, dest_dir)

    return


if __name__ == "__main__":
    main()
