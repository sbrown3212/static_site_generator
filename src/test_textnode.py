import unittest

from textnode import TextNode, TextType


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
        # self.assertEqual("TextNode(This is a test node, italic, https://boot.dev", repr(node))
        self.assertEqual("TextNode(This is a test node, italic, https://boot.dev", node.__repr__())


if __name__ == "__main__":
    unittest.main()