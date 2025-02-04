
def markdown_to_blocks(markdown): 
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