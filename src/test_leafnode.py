import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual("<p>This is a paragraph of text.</p>", node.to_html())

    def test_to_html2(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')
    
    # From Boots
    def test_props_multiple(self):
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