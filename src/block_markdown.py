from enum import Enum

import re


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


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block): # takes a single block
    # Headings
    def is_heading(block):
        pattern = r"^#{1,6} "
        match = re.match(pattern, block)
        return match
    
    if is_heading(block):
        return BlockType.HEADING

    # if block[0] == "#":
    #     return BlockType.HEADING
    
    if block[0:3] == "```" and block[-3:] == "```":
        return BlockType.CODE
    
    def is_quote(block):
        lines = block.split("\n")

        for line in lines:
            if line[0] != ">":
                return False
        
        return True
        
    if is_quote(block):
        return BlockType.QUOTE
    
    def is_unorder_list(block):
        lines = block.split("\n")

        for line in lines:
            # if first character is not "*" or "-" followed by a space
            if not re.match(r"^[\*-] ", line):
                return False
        
        return True

    if is_unorder_list(block):
        return BlockType.UNORDERED_LIST
    
    def is_ordered_list(block):
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
        
    if is_ordered_list(block):
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH