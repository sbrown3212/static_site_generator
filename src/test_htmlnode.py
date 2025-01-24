import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node_props = {"href": "https://www.google.com", "target": "_blank",}
        node = HTMLNode(props=node_props)
        self.assertEqual(
            ' href="https://www.google.com" target="_blank"', node.props_to_html()
        )

    def test_props_to_html2(self):
        node = HTMLNode()
        self.assertEqual("", node.props_to_html())
    
    def test_props_to_html3(self):
        node_props = {"href": "https://www.google.com"}
        node = HTMLNode(props=node_props)
        self.assertEqual(' href="https://www.google.com"', node.props_to_html())
    
    def test_repr(self):
        node = HTMLNode()
        self.assertEqual('HTMLNode(None, None, None, None)', repr(node))
    
    def test_repr2(self):
        node = HTMLNode(value="this is a test html node")
        self.assertEqual('HTMLNode(None, this is a test html node, None, None)', repr(node))


if __name__ == "__main__":
    unittest.main()