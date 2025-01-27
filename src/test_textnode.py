import unittest

from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import LeafNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)
    
    def test_not_eq2(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("this is a test node", TextType.TEXT)
        self.assertNotEqual(node, node2)
    
    def test_url_default(self):
        node = TextNode("This is a test node", TextType.BOLD)
        expected_url = None
        self.assertEqual(node.url, expected_url)

    def test_repr(self):
        node = TextNode("This is a test node", TextType.ITALIC, "https://boot.dev")
        self.assertEqual("TextNode(This is a test node, italic, https://boot.dev", node.__repr__())

    # Text node to html node tests
    def test_text_node_to_html_node_TEXT(self):
        text_node = TextNode("Normal text", TextType.TEXT)
        leaf_node = LeafNode(None, "Normal text")
        result = text_node_to_html_node(text_node)
        self.assertEqual(result, leaf_node)

    def test_text_node_to_html_node_BOLD(self):
        text_node = TextNode("Bold text", TextType.BOLD)
        leaf_node = LeafNode("b", "Bold text")
        result = text_node_to_html_node(text_node)
        self.assertEqual(result, leaf_node)

    def test_text_node_to_html_node_LINK(self):
        text_node = TextNode("Link text", TextType.LINK, "https://boot.dev")
        leaf_node = LeafNode("a", "Link text", props={"href": "https://boot.dev"})
        result = text_node_to_html_node(text_node)
        self.assertEqual(result, leaf_node)
    
    def test_text_node_to_html_node_IMAGE(self):
        text_node = TextNode("Image alt text", TextType.IMAGE, "assets/example.img")
        leaf_node = LeafNode("img", "", props={"src": "assets/example.img", "alt": "Image alt text"})
        result = text_node_to_html_node(text_node)
        self.assertEqual(result, leaf_node)

if __name__ == "__main__":
    unittest.main()