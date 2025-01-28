from textnode import TextNode, TextType

# Takes a list of "old_nodes", a delimiter, and a text type
# returns a list of nodes (old_nodes split and then formatted by the delimiter)
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    # Initialize variable to store new nodes
    new_nodes = []

    # Iterate over list of old nodes
    for old_node in old_nodes:
        # If node is not "TEXT" text type, then add it as is to `new_nodes`
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        
        # Split the current node by `delimiter`
        parts = old_node.text.split(delimiter)

        # If length of parts is even (closing delimiter is missing) raise an exception
        if len(parts) % 2 == 0:
            raise Exception("Invalid markdown syntax. Formatted text not closed")
        
        # Iterate over split parts of `old_node`
        for i in range(len(parts)):
            # Skip if current element is blank (delimiter found at first or last index)
            if parts[i] == "":
                continue
            
            if i % 2 == 0: # Even indices are plain text 
                new_nodes.append(
                    TextNode(parts[i], TextType.TEXT)
                )
            else: # Odd indices are formatted according to the `text_type` argument
                new_nodes.append(
                    TextNode(parts[i], text_type)
                )

    return new_nodes
        