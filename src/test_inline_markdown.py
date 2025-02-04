import unittest

from inline_markdown import split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link, text_to_textnodes
from textnode import TextNode, TextType


class TextSplitNodesDelimiter(unittest.TestCase):
    # Split nodes delimiter
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
        self.assertEqual(result, expected)

    # Extract markdown images
    def test_extract_markdown_images_multiple(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        result = extract_markdown_images(text)
        self.assertEqual(
            result,
            [
                ("rick roll", "https://i.imgur.com/aKaOqIh.gif"), 
                ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")
            ]
        )

    def test_extract_markdown_images_single(self):
        text = "This is text with only a ![rick roll](https://i.imgur.com/aKaOqIh.gif)"
        result = extract_markdown_images(text)
        self.assertEqual(
            result,
            [("rick roll", "https://i.imgur.com/aKaOqIh.gif")]
        )
    
    def test_extract_markdown_images_none(self):
        text = "This is text without an image in markdown syntax"
        result = extract_markdown_images(text)
        self.assertEqual(result, [])
    
    def test_extract_markdown_images_w_mixed(self):
        text = "This is text with a [rick roll](https://i.imgur.com/aKaOqIh.gif) link and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg) image"
        result = extract_markdown_images(text)
        self.assertEqual(result, [("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")])

    # Extract markdown links
    def test_extract_markdown_links_multiple(self):
        text = "This is text with a [rick roll](https://i.imgur.com/aKaOqIh.gif) and [obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        result = extract_markdown_links(text)
        # print("result: ", result)
        self.assertEqual(
            result,
            [
                ("rick roll", "https://i.imgur.com/aKaOqIh.gif"), 
                ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")
            ]
        )

    def test_extract_markdown_links_single(self):
        text = "This is text with only a [rick roll](https://i.imgur.com/aKaOqIh.gif)"
        result = extract_markdown_links(text)
        self.assertEqual(
            result,
            [("rick roll", "https://i.imgur.com/aKaOqIh.gif")]
        )
    
    def test_extract_markdown_links_none(self):
        text = "This is text without a link in markdown syntax"
        result = extract_markdown_links(text)
        self.assertEqual(result, [])

    def test_extract_markdown_links_mixed(self):
        text = "This is text with a [rick roll](https://i.imgur.com/aKaOqIh.gif) link and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg) image"
        result = extract_markdown_links(text)
        self.assertEqual(result, [("rick roll", "https://i.imgur.com/aKaOqIh.gif")])
    
    # Split nodes image
    def test_split_nodes_image_single(self):
        node = TextNode(
            "This is text with only a ![rick roll](https://i.imgur.com/aKaOqIh.gif)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        expected = [
                TextNode("This is text with only a ", TextType.TEXT),
                TextNode("rick roll", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif"),
            ]

        self.assertEqual(expected, new_nodes)
    
    def test_split_nodes_image_single2(self):
        node = TextNode(
            "This is text with only a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and some text afterward",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        expected = [
                TextNode("This is text with only a ", TextType.TEXT),
                TextNode("rick roll", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif"),
                TextNode(" and some text afterward", TextType.TEXT),
            ]

        self.assertEqual(expected, new_nodes)
    
    def test_split_nodes_image_repeat_image(self):
        node = TextNode(
            "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif), and another ![rick roll](https://i.imgur.com/aKaOqIh.gif)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        expected = [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("rick roll", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif"),
                TextNode(", and another ", TextType.TEXT),
                TextNode("rick roll", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif"),
            ]

        self.assertEqual(expected, new_nodes)

    def test_split_nodes_image_no_image(self):
        node = TextNode(
            "This is only text without any images",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        expected = [
                TextNode("This is only text without any images", TextType.TEXT),
            ]

        self.assertEqual(expected, new_nodes)

    def test_split_nodes_image_mixed(self):
        node = TextNode(
            "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif), and a link [to boot dev](https://boot.dev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        expected = [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("rick roll", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif"),
                TextNode(", and a link [to boot dev](https://boot.dev)", TextType.TEXT),
            ]
        self.assertEqual(expected, new_nodes)
    
    #Split Nodes link
    def test_split_nodes_link(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertEqual(
            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode(
                    "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
                ),
            ],
            new_nodes
        )

    def test_split_nodes_link_repeat_link(self):
        node = TextNode(
            "This is a [link to boot dev](https://boot.dev), and another [link to boot dev](https://boot.dev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        expected = [
                TextNode("This is a ", TextType.TEXT),
                TextNode("link to boot dev", TextType.LINK, "https://boot.dev"),
                TextNode(", and another ", TextType.TEXT),
                TextNode("link to boot dev", TextType.LINK, "https://boot.dev"),
            ]

        self.assertEqual(expected, new_nodes)
    
    def test_split_nodes_image_no_link(self):
        node = TextNode(
            "This is only text without any links",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        expected = [
                TextNode("This is only text without any links", TextType.TEXT),
            ]

        self.assertEqual(expected, new_nodes)

    def test_split_nodes_link_mixed(self):
        node = TextNode(
            "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif), and a link [to boot dev](https://boot.dev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        expected = [
                TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif), and a link ", TextType.TEXT),
                TextNode("to boot dev", TextType.LINK, "https://boot.dev"),
            ]
        self.assertEqual(expected, new_nodes)
    
    def test_split_nodes_link_single(self):
        node = TextNode(
            "This is a link to [boot dev](https://boot.dev) and some text afterward",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        expected = [
                TextNode("This is a link to ", TextType.TEXT),
                TextNode("boot dev", TextType.LINK, "https://boot.dev"),
                TextNode(" and some text afterward", TextType.TEXT),
            ]

        self.assertEqual(expected, new_nodes)
    
    # Text to textnodes
    def test_text_to_textnodes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"

        actual = text_to_textnodes(text)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        self.assertEqual(actual, expected)