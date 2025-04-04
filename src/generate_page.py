import os

from markdown_to_html import markdown_to_html_nodes


def extract_title(markdown):
    line_one = markdown.split("\n", 1)[0]

    if line_one[0:2] != "# ":
        raise Exception("Invalid title markdown")
    
    title = line_one[1:].strip()
    return title


def generate_page(from_path, dest_path, template_path):
    print("-----")
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    # Open and read markdown file
    try:
        with open(from_path, "r") as markdown:
            markdown_data = markdown.read()
    except Exception as e:
        raise Exception(f"Failed to read markdown from {from_path}:\n{str(e)}")
    
    # Open and read HTML template file
    try:
        with open(template_path, "r") as template:
            template_data = template.read()
    except Exception as e:
        raise Exception(f"Failed to read template from {template_path}")
    
    # Generate raw HTML from markdown to be used as 'content' in HTML template
    html_nodes = markdown_to_html_nodes(markdown_data)
    html = html_nodes.to_html()

    # Extract title from markdown to be used as 'title' in HTML template
    title = extract_title(markdown_data)

    # Insert 'title' and 'content' into template 
    html_page = template_data.replace("{{ Title }}", title).replace("{{ Content }}", html)

    # Write 'html_page' to 'index.html'
    try:
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)

        with open(dest_path, "w") as file:
            file.write(html_page)
    except Exception as e:
        raise Exception(f"Failed to write {dest_path}:\n{str(e)}")
