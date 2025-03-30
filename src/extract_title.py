

def extract_title(markdown):
    line_one = markdown.split("\n", 1)[0]

    if line_one[0:2] != "# ":
        raise Exception("Invalid title markdown")
    
    title = line_one[1:].strip()
    return title