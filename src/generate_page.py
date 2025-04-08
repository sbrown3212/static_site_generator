import os

from markdown_to_html import markdown_to_html_nodes


def extract_title(markdown):
    # Get first line
    line_one = markdown.split("\n", 1)[0]

    # Ensure first line is h1 heading
    if line_one[0:2] != "# ":
        raise Exception("Invalid title markdown")
    
    # Remove markdown syntax and return title
    title = line_one[1:].strip()
    return title


def generate_pages_recursive(content_dir_path, template_contents, dest_dir_path):
    # Get contents of content directory
    if os.path.exists(content_dir_path):
        contents = os.listdir(content_dir_path)
    else:
        raise Exception(f"Content directory path '{content_dir_path}' not found")
    
    # Iterate through contents of content directory
    for item in contents:
        # Set paths for item
        content_item_path = os.path.join(content_dir_path, item)
        dest_item_path = os.path.join(dest_dir_path, item)

        # Check if item is a directory
        if os.path.isdir(content_item_path):
            # If item is a directory, ensure 'dest_item_path' exists
            # and recursively call function again
            os.makedirs(dest_item_path, exist_ok=True)
            generate_pages_recursive(content_item_path, template_contents, dest_item_path)
        
        elif item.endswith('.md'): # only generate html if item is markdown file
            # Open and read markdown file
            with open(content_item_path, "r") as file:
                md_content = file.read()
            
            # generate title
            title = extract_title(md_content)

            # generate html content
            html_nodes = markdown_to_html_nodes(md_content)
            content = html_nodes.to_html()

            # update template with title and content
            html_page = template_contents.replace("{{ Title }}", title).replace("{{ Content }}", content)

            # Update destination path to have .html extension rather than .md
            dest_item_path = dest_item_path.replace(".md", ".html")

            # ensure 'dest_item_path' exists
            os.makedirs(os.path.dirname(dest_item_path), exist_ok=True) # QUESTION: does this work if dest_item_path is a file?
            # write html content to destination
            with open(dest_item_path, "w") as file:
                file.write(html_page)
            

def generate_all_pages(content_dir_path, template_path, dest_dir_path):
    # Open and read template file
    try:
        with open(template_path, "r") as file:
            template_content = file.read()
    except:
        raise Exception(f"Failed to read contents of '{template_path}' path")

    generate_pages_recursive(content_dir_path, template_content, dest_dir_path)