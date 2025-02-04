import unittest

from block_markdown import markdown_to_blocks


class TestBlockMarkdown(unittest.TestCase):
    # Markdown to blocks
    def test_markdown_to_blocks(self):
        markdown = ("""# This is a heading

        This is a paragraph of text. It has some **bold** and *italic* words inside of it.

        * This is the first list item in a list block
        * This is a list item
        * This is another list item""")
        results = markdown_to_blocks(markdown)
        expected = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            """* This is the first list item in a list block
* This is a list item
* This is another list item""",
        ]
        self.assertEqual(results, expected)
    
    def test_markdown_to_blocks2(self):
        markdown = ""
        result = markdown_to_blocks(markdown)
        expected = []
        self.assertEqual(result, expected)
    
    def test_markdown_to_blocks_excessive_lines(self):
        markdown = """This is a block followed by excessive new lines.\n\n\n\nThis is another block."""

        result = markdown_to_blocks(markdown)
        expected = [
            "This is a block followed by excessive new lines.",
            "This is another block.",
        ]
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()