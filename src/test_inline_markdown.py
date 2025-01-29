import unittest

from inline_markdown import split_nodes_delimiter, extract_markdown_images, extract_markdown_links
from textnode import TextNode, TextType


class TextSplitNodesDelimiter(unittest.TestCase):
    # Split nodes delimiter
    def test_node_split_bold(self):
        old_nodes = [
            TextNode("This is a **bold** word", TextType.TEXT)
        ]
        new_nodes = [
            TextNode("This is a ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" word", TextType.TEXT)
        ]
        self.assertEqual(
            split_nodes_delimiter(old_nodes, "**", TextType.BOLD),
            new_nodes
        )

    def test_node_split_italic(self):
        old_nodes = [
            TextNode("This is an *italic* word", TextType.TEXT)
        ]
        new_nodes = [
            TextNode("This is an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word", TextType.TEXT)
        ]
        self.assertEqual(
            split_nodes_delimiter(old_nodes, "*", TextType.ITALIC),
            new_nodes
        )

    def test_node_split_code(self):
        old_nodes = [
            TextNode("This is a `code` word", TextType.TEXT)
        ]
        new_nodes = [
            TextNode("This is a ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" word", TextType.TEXT)
        ]
        self.assertEqual(
            split_nodes_delimiter(old_nodes, "`", TextType.CODE),
            new_nodes
        )

    def test_node_split_no_closing_delimiter(self):
        with self.assertRaises(Exception):
            old_nodes = [
                TextNode("This is a **bold word", TextType.TEXT)
            ]
            split_nodes_delimiter(old_nodes, "**", TextType.BOLD)

    def test_node_split_multiple_bold(self):
        old_nodes = [
            TextNode("This is a **bold** word. And another **bold** word.", TextType.TEXT)
        ]
        new_nodes = [
            TextNode("This is a ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" word. And another ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" word.", TextType.TEXT)
        ]
        self.assertEqual(
            split_nodes_delimiter(old_nodes, "**", TextType.BOLD),
            new_nodes
        )

    def test_node_split_bold_and_italic(self):
        old_nodes = [
            TextNode("This is a **bold** word. And an *italicized* word.", TextType.TEXT)
        ]
        bold_delimited = split_nodes_delimiter(old_nodes, "**", TextType.BOLD)
        result = split_nodes_delimiter(bold_delimited, "*", TextType.ITALIC)

        expected = [
            TextNode("This is a ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" word. And an ", TextType.TEXT),
            TextNode("italicized", TextType.ITALIC),
            TextNode(" word.", TextType.TEXT)
        ]
        self.assertEqual(result, expected)

    # Extract markdown images
    def test_extract_markdown_images_multiple(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        result = extract_markdown_images(text)
        self.assertEqual(
            result,
            [
                ("rick roll", "https://i.imgur.com/aKaOqIh.gif"), 
                ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")
            ]
        )

    def test_extract_markdown_images_single(self):
        text = "This is text with only a ![rick roll](https://i.imgur.com/aKaOqIh.gif)"
        result = extract_markdown_images(text)
        self.assertEqual(
            result,
            [("rick roll", "https://i.imgur.com/aKaOqIh.gif")]
        )
    
    def test_extract_markdown_images_none(self):
        text = "This is text without an image in markdown syntax"
        result = extract_markdown_images(text)
        self.assertEqual(result, [])
    
    def test_extract_markdown_images_w_mixed(self):
        text = "This is text with a [rick roll](https://i.imgur.com/aKaOqIh.gif) link and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg) image"
        result = extract_markdown_images(text)
        self.assertEqual(result, [("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")])

    # Extract markdown links
    def test_extract_markdown_links_multiple(self):
        text = "This is text with a [rick roll](https://i.imgur.com/aKaOqIh.gif) and [obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        result = extract_markdown_links(text)
        # print("result: ", result)
        self.assertEqual(
            result,
            [
                ("rick roll", "https://i.imgur.com/aKaOqIh.gif"), 
                ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")
            ]
        )

    def test_extract_markdown_links_single(self):
        text = "This is text with only a [rick roll](https://i.imgur.com/aKaOqIh.gif)"
        result = extract_markdown_links(text)
        self.assertEqual(
            result,
            [("rick roll", "https://i.imgur.com/aKaOqIh.gif")]
        )
    
    def test_extract_markdown_links_none(self):
        text = "This is text without a link in markdown syntax"
        result = extract_markdown_links(text)
        self.assertEqual(result, [])

    def test_extract_markdown_links_mixed(self):
        text = "This is text with a [rick roll](https://i.imgur.com/aKaOqIh.gif) link and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg) image"
        result = extract_markdown_links(text)
        self.assertEqual(result, [("rick roll", "https://i.imgur.com/aKaOqIh.gif")])