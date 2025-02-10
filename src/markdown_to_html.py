from block_markdown import markdown_to_blocks, block_to_block_type
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node
from htmlnode import ParentNode, LeafNode


def text_to_children(text) :
    text_nodes = text_to_textnodes(text)

    children = list(map(text_node_to_html_node, text_nodes))
    
    return children


def paragraph_block_to_html_node(block):
    children = text_to_children(block)

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
    lines = block.split("\n")

    # Map over lines, using line text (skipping first character)
    # as input in `text_to_children` function,
    # and put that(those) node(s) as children in a parent "p" block node
    children = list(map(
        lambda line: ParentNode("p", text_to_children(line[1:])),
        lines
    ))

    quote_block_node = ParentNode("blockquote", children)

    return quote_block_node


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
                pass

            case "ordered_list":
                pass

            case _:
                raise Exception("Invalid block type")
        
    parent_html_node = ParentNode("div", html_nodes)

    return parent_html_node