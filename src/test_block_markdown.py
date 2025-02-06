import unittest

from block_markdown import (
    markdown_to_blocks,
    block_to_block_type,
    block_type_paragraph,
    block_type_heading,
    block_type_code,
    block_type_quote,
    block_type_ulist,
    block_type_olist
)


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
    
    # Block to block type
    def test_block_to_block_type_heading(self):
        block = "# This is a heading"
        result = block_to_block_type(block)
        expected = block_type_heading
        self.assertEqual(result, expected)
    
    def test_block_to_block_type_heading2(self):
        block = "### This is a heading"
        result = block_to_block_type(block)
        expected = block_type_heading
        self.assertEqual(result, expected)
    
    def test_block_to_block_type_heading3(self):
        block = "####### This is not a heading"
        result = block_to_block_type(block)
        expected = block_type_paragraph
        self.assertEqual(result, expected)
    
    def test_block_to_block_type_heading4(self):
        block = "#This is not a heading"
        result = block_to_block_type(block)
        expected = block_type_paragraph
        self.assertEqual(result, expected)

    def test_block_to_block_type_code(self):
        block = "```This is a code block```"
        result = block_to_block_type(block)
        expected = block_type_code
        self.assertEqual(result, expected)
    
    def test_block_to_block_type_code2(self):
        block = "```This is a code block\nwith multiple\nlines```"
        result = block_to_block_type(block)
        expected = block_type_code
        self.assertEqual(result, expected)

    def test_block_to_block_type_quote(self):
        block = "> This is a quote block"
        result = block_to_block_type(block)
        expected = block_type_quote
        self.assertEqual(result, expected)
    
    def test_block_to_block_type_quote2(self):
        block = "> This is a quote block\n> with multiple\n> lines"
        result = block_to_block_type(block)
        expected = block_type_quote
        self.assertEqual(result, expected)
    
    def test_block_to_block_type_unordered(self):
        block = "* here\n* is\n* a\n* list\n* of\n* words"
        result = block_to_block_type(block)
        expected = block_type_ulist
        self.assertEqual(result, expected)
    
    def test_block_to_block_type_unordered2(self):
        block = "* here\n- is\n* a\n* list\n- of\n* words"
        result = block_to_block_type(block)
        expected = block_type_ulist
        self.assertEqual(result, expected)

    def test_block_to_block_type_ordered(self):
        block = "1. one\n2. two\n3. three\n4. four\n5. five\n6. six\n7. seven\n8. eight\n9. nine\n10. ten"
        result = block_to_block_type(block)
        expected = block_type_olist
        self.assertEqual(result, expected)
    
    def test_block_to_block_type_paragraph(self):
        block = "this is a paragraph"
        result = block_to_block_type(block)
        expected = block_type_paragraph
        self.assertEqual(result, expected)
    
    def test_block_to_block_type_paragraph2(self):
        block = "1. one\n3. not two\n3. three"
        result = block_to_block_type(block)
        expected = block_type_paragraph
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()