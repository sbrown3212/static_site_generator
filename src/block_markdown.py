import re

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_ulist = "unordered_list"
block_type_olist = "ordered_list"


def markdown_to_blocks(markdown): 
    # # Solution from boot.dev
    # blocks = markdown.split("\n\n")
    # filtered_blocks = []
    # for block in blocks:
    #     if block == "":
    #         continue
    #     block = block.strip()
    #     filtered_blocks.append(block)
    # return filtered_blocks

    parts = markdown.split("\n")

    block_list = []
    current_block = ""

    for i in range(len(parts)):
        # 
        line = parts[i].strip()

        # Prevent excessive empty lines from being added as blocks
        if line == "":
            continue

        current_block += line

        # if iterating over last element (line) of `parts` list
        if i == len(parts) - 1:
            block_list.append(current_block)
            current_block = ""
            continue

        # if current element (line) is the end of current block
        if parts[i + 1] == "":
            block_list.append(current_block)
            current_block = ""
            i += 1
        else: # if block is not finished
            current_block += "\n"

    return block_list


def is_block_heading(block):
    pattern = r"^#{1,6} "
    match = re.match(pattern, block)
    return match

def is_block_quote(block):
    lines = block.split("\n")
    # From Boots at boot.dev
    return all(line.startswith(">") for line in lines)

def is_block_unorder_list(block):
    lines = block.split("\n")
    # From Boots at boot.dev
    return all(re.match(r"^[\*-] ", line) for line in lines)

def is_block_ordered_list(block):
    lines = block.split("\n")

    count = 1
    pattern = r"^(\d+)\. "
    for line in lines:
        match = re.match(pattern, line)
        if not match:
            return False
        
        number = int(match.group(1))
        if number != count:
            return False
        
        count += 1
    
    return True

def block_to_block_type(block): # takes a single block
    # Heading block
    if is_block_heading(block):
        return block_type_heading
    
    # Code block
    if block[0:3] == "```" and block[-3:] == "```":
        return block_type_code
    
    # Quote block
    if is_block_quote(block):
        return block_type_quote
    
    # Unorderded list block
    if is_block_unorder_list(block):
        return block_type_ulist
    
    # Orderded list block
    if is_block_ordered_list(block):
        return block_type_olist

    # Everything else
    return block_type_paragraph