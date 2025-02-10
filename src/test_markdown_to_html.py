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


if __name__ == "__main__":
    unittest.main()
