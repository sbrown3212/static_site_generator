import unittest

from split_nodes_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType


class TextSplitNodesDelimiter(unittest.TestCase):
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
        print("")
        print("  actual: ", result)
        print("expected: ", expected)
        self.assertEqual(result, expected)