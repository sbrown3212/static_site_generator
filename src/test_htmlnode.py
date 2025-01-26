import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    # HTMLNode tests
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

    # LeafNode tests
    def test_to_html(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual("<p>This is a paragraph of text.</p>", node.to_html())

    def test_to_html2(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')
    
    def test_props_multiple(self): # From Boots
        node = LeafNode("p", "Hello", {"class": "greeting", "id": "hello"})
        # print(f"Node props: {node.props}")  # Debug print
        result = node.props_to_html()
        # print(f"Actual result: '{result}'")
        self.assertTrue(
            result == ' class="greeting" id="hello"' or 
            result == ' id="hello" class="greeting"'
        )


if __name__ == "__main__":
    unittest.main()