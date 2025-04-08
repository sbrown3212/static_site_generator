from block_markdown import markdown_to_blocks, block_to_block_type
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node
from htmlnode import ParentNode, LeafNode


def text_to_children(text) :
    text_nodes = text_to_textnodes(text)

    children = list(map(text_node_to_html_node, text_nodes))
    
    return children


def paragraph_block_to_html_node(block):
    # Remove all line braking spaces
    lines = block.split("\n")
    paragraph = " ".join(lines)

    children = text_to_children(paragraph)

    paragraph_node = ParentNode("p", children)

    return paragraph_node


def heading_block_to_html_node(block):
    block_split = block.split(" ", 1)
    heading_num = len(block_split[0])
    text = block_split[1]

    children = text_to_children(text)
    
    heading_block = ParentNode(f"h{heading_num}", children)
    
    return heading_block


def code_block_to_html_node(block):
    text = block.replace("```", "")
    children = text_to_children(text)

    code_block_node = ParentNode(
        "pre", [
            ParentNode("code", children)
        ]
    )

    return code_block_node


def quote_block_to_html_node(block):
    # split block by line breaks
    lines = block.split("\n")

    # ------

    # This solution passes the test from boot.dev by combining quote text into
    # one block and wraps it in a '<blockquote>' instead of wrapping the 
    # collection of '<p>' tags within a '<blockquote>'
    
    # Remove '>' characters and white space from each line
    sanitized_lines = []

    for line in lines:
        if not line.strip():
            continue
        sanitized_lines.append(line[1:].strip())

    # Join lines into one block
    quote = " ".join(sanitized_lines)

    # Create quote block node
    quote_block_node = LeafNode("blockquote", quote)

    #  -------

    # This was the original solution, but does not pass because
    # test expects no '<p>' tag between '<blockquote>' tag and quote text

    # # Map over lines, using line text (skipping first character)
    # # as input in `text_to_children` function,
    # # and put that(those) node(s) as children in a parent "p" block node
    # def process_line(line):
    #     # if line[1:].strip():
    #     #     return line[1:].strip()
    #     # return None
    #     if line == ">":
    #         return None
    #     return line[1:].strip()
    
    # processed_lines = list(map(process_line, lines))

    # filtered_lines = []

    # for line in processed_lines:
    #     if line is not None:
    #         filtered_lines.append(line)

    # children = list(map(
    #     lambda line: ParentNode("p", text_to_children(line[1:])),
    #     # processed_lines
    #     filtered_lines
    # ))

    # quote_block_node = ParentNode("blockquote", children)

    # -------

    return quote_block_node


def unordered_list_block_to_html_node(block):
    lines = block.split("\n")

    list_item_nodes = list(map(
        lambda line: ParentNode("li", text_to_children(line[2:].strip())),
        lines
    ))

    ulist_block_node = ParentNode("ul", list_item_nodes)

    return ulist_block_node

def ordered_list_block_to_html_node(block):
    lines = block.split("\n")

    list_item_nodes = list(map(
        lambda line: ParentNode("li", text_to_children(line[3:].strip())),
        lines
    ))

    olist_block_node = ParentNode("ol", list_item_nodes)

    return olist_block_node


def markdown_to_html_nodes(markdown):
    blocks = markdown_to_blocks(markdown)

    html_nodes = []

    for block in blocks:
        block_type = block_to_block_type(block)

        match (block_type):
            case "paragraph":
                paragraph_block_node = paragraph_block_to_html_node(block)
                html_nodes.append(paragraph_block_node)
                continue

            case "heading":
                heading_block_node = heading_block_to_html_node(block)
                html_nodes.append(heading_block_node)
                continue

            case "code":
                code_block_node = code_block_to_html_node(block)
                html_nodes.append(code_block_node)
                continue

            case "quote":
                quote_block_node = quote_block_to_html_node(block)
                html_nodes.append(quote_block_node)
                continue

            case "unordered_list":
                ulist_block_node = unordered_list_block_to_html_node(block)
                html_nodes.append(ulist_block_node)
                continue

            case "ordered_list":
                olist_block_node = ordered_list_block_to_html_node(block)
                html_nodes.append(olist_block_node)
                continue

            case _:
                raise Exception("Invalid block type")
        
    parent_html_node = ParentNode("div", html_nodes)

    return parent_html_node