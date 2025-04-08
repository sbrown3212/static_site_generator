from textnode import *
from generate_page import generate_all_pages

import os
import shutil


STATIC_PATH = r"./static"
PUBLIC_PATH = r"./public"
CONTENT_PATH = r"./content"
TEMPLATE_PATH = r"./template.html"

def delete_dir_contents(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Path '{path}' does not exist.")
    
    if not os.path.isdir(path):
        raise ValueError(f"Path '{path}' is not a directory.")
    
    contents = os.listdir(path)
    for item in contents:
        item_path = os.path.join(path, item)
        if os.path.isfile(item_path):
            os.remove(item_path)
        else:
            shutil.rmtree(item_path)


# Recursive function to copy contents w/o using 'shutil.copytree'
def copy_contents_recursive(source_dir, dest_dir):
    # Ensure dest_dir exists
    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)

    for item in os.listdir(source_dir):
        source_path = os.path.join(source_dir, item)
        dest_path = os.path.join(dest_dir, item)

        if os.path.isfile(source_path):
            shutil.copy(source_path, dest_path)
        else:
            copy_contents_recursive(source_path, dest_path)



def copy_dir(source_dir, dest_dir):
    if not os.path.exists(source_dir):
        raise ValueError(f"Source path '{source_dir}' does not exist.")

    os.makedirs(dest_dir, exist_ok=True)
    delete_dir_contents(dest_dir) #clean dest_dir before copying
    
    try:
        copy_contents_recursive(source_dir, dest_dir)
    except:
        raise Exception("Failed to copy contents")
    

def main():
    copy_dir(STATIC_PATH, PUBLIC_PATH)

    generate_all_pages(CONTENT_PATH, TEMPLATE_PATH, PUBLIC_PATH)


if __name__ == "__main__":
    main()
