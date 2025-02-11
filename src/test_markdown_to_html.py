import unittest

from markdown_to_html import markdown_to_html_nodes
from htmlnode import ParentNode, LeafNode


class TestMarkdownToHTML(unittest.TestCase):
    def test_markdown_to_html_nodes_paragraph(self):
        markdown = "This is a paragraph"
        result = markdown_to_html_nodes(markdown)
        expected = ParentNode("div", [
            ParentNode("p", [
                LeafNode(None, "This is a paragraph")
            ])
        ])
        self.assertEqual(result, expected)

    def test_markdown_to_html_nodes_heading(self):
        markdown = "### This is an 'h3' heading"
        result = markdown_to_html_nodes(markdown)
        expected = ParentNode("div", [
            ParentNode("h3", [
                LeafNode(None, "This is an 'h3' heading")
            ])
        ])
        self.assertEqual(expected, result)
    
    def test_markdown_to_html_nodes_code(self):
        markdown = "```This is a code block```"
        result = markdown_to_html_nodes(markdown)
        expected = ParentNode(
            "div", [
                ParentNode("pre", [
                    ParentNode("code", [
                        LeafNode(None, "This is a code block")
                    ])
                ])
            ]
        )
        self.assertEqual(expected, result)

    def test_markdown_to_html_nodes_quote(self):
        markdown = ">This is a quote"
        result = markdown_to_html_nodes(markdown)
        expected = ParentNode(
            "div", [
                ParentNode("blockquote", [
                    ParentNode("p", [
                        LeafNode(None, "This is a quote")
                    ])    
                ])
            ]
        )
        self.assertEqual(expected, result)

    def test_markdown_to_html_nodes_quote2(self):
        markdown = ">This is a multi line quote.\n>This is the second line."
        result = markdown_to_html_nodes(markdown)
        expected = ParentNode(
            "div", [
                ParentNode("blockquote", [
                    ParentNode("p", [LeafNode(None, "This is a multi line quote.")]),
                    ParentNode("p", [LeafNode(None, "This is the second line.")])
                ])
            ]
        )
        self.assertEqual(expected, result)
    
    def test_markdown_to_html_nodes_quote3(self):
        markdown = ">This is a multi line quote.\n>This second line has an inline `code` element."
        result = markdown_to_html_nodes(markdown)
        expected = ParentNode(
            "div", [
                ParentNode("blockquote", [
                    ParentNode("p", [LeafNode(None, "This is a multi line quote.")]),
                    ParentNode("p", [
                        LeafNode(None, "This second line has an inline "),
                        LeafNode("code", "code"),
                        LeafNode(None, " element.")
                    ])
                ])
            ]
        )
        self.assertEqual(expected, result)
    
    def test_markdown_to_html_nodes_ulist(self):
        markdown = "* Line one\n* Line two\n* Line three"
        result = markdown_to_html_nodes(markdown)
        expected = ParentNode("div", [
            ParentNode("ul", [
                ParentNode("li", [LeafNode(None, "Line one")]),
                ParentNode("li", [LeafNode(None, "Line two")]),
                ParentNode("li", [LeafNode(None, "Line three")])
            ])
        ])
        self.assertEqual(expected, result)
    
    def test_markdown_to_html_nodes_olist(self):
        markdown = "1. Line one\n2. Line two\n3. Line three"
        result = markdown_to_html_nodes(markdown)
        expected = ParentNode("div", [
            ParentNode("ol", [
                ParentNode("li", [LeafNode(None, "Line one")]),
                ParentNode("li", [LeafNode(None, "Line two")]),
                ParentNode("li", [LeafNode(None, "Line three")])
            ])
        ])
        self.assertEqual(expected, result)

    def test_markdown_to_html_nodes_combined(self):
        markdown = "### This is an h3 heading\n\nThis is a paragraph.\n\n* This is the first item in an unordered list\n* This is the second item in an unordered list\n* This is the third item in an unordered list"
        result = markdown_to_html_nodes(markdown)
        expected = ParentNode("div", [
            ParentNode("h3", [LeafNode(None, "This is an h3 heading")]),
            ParentNode("p", [LeafNode(None, "This is a paragraph.")]),
            ParentNode("ul", [
                ParentNode("li", [LeafNode(None, "This is the first item in an unordered list")]),
                ParentNode("li", [LeafNode(None, "This is the second item in an unordered list")]),
                ParentNode("li", [LeafNode(None, "This is the third item in an unordered list")]),
            ])
        ])
        self.assertEqual(expected, result)
    
    def test_markdown_to_html_nodes_combined2(self):
        markdown = "# This is an h1 heading\n\nThis is a paragraph.\n\n1. This is the first item in an ordered list\n2. This is the second item in an ordered list\n3. This is the third item in an ordered list\n\n```This is a code block```"
        result = markdown_to_html_nodes(markdown)
        expected = ParentNode("div", [
            ParentNode("h1", [LeafNode(None, "This is an h1 heading")]),
            ParentNode("p", [LeafNode(None, "This is a paragraph.")]),
            ParentNode("ol", [
                ParentNode("li", [LeafNode(None, "This is the first item in an ordered list")]),
                ParentNode("li", [LeafNode(None, "This is the second item in an ordered list")]),
                ParentNode("li", [LeafNode(None, "This is the third item in an ordered list")]),
            ]),
            ParentNode("pre", [
                ParentNode("code", [LeafNode(None, "This is a code block")])
            ])
        ])
        self.assertEqual(expected, result)
    
    def test_markdown_to_html_nodes_combined3(self):
        markdown = "# This is an h1 heading\n\nThis is a paragraph. It has *italic*, **bold**, and `code` text in it.\n\n```This is a code block```"
        result = markdown_to_html_nodes(markdown)
        expected = ParentNode("div", [
            ParentNode("h1", [LeafNode(None, "This is an h1 heading")]),
            ParentNode("p", [
                LeafNode(None, "This is a paragraph. It has "),
                LeafNode("i", "italic"),
                LeafNode(None, ", "),
                LeafNode("b", "bold"),
                LeafNode(None, ", and "),
                LeafNode("code", "code"),
                LeafNode(None, " text in it."),
            ]),
            ParentNode("pre", [
                ParentNode("code", [LeafNode(None, "This is a code block")])
            ])
        ])
        self.assertEqual(expected, result)
    
    def test_markdown_to_html_nodes_combined4(self):
        markdown = "# This is an h1 heading\n\nThis \nparagraph \nis \none \nnode \nand \nis \non \none \nline.\n\n```This is a code block```"
        result = markdown_to_html_nodes(markdown)
        expected = ParentNode("div", [
            ParentNode("h1", [LeafNode(None, "This is an h1 heading")]),
            ParentNode("p", [
                LeafNode(None, "This paragraph is one node and is on one line.")
            ]),
            ParentNode("pre", [
                ParentNode("code", [LeafNode(None, "This is a code block")])
            ])
        ])
        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
