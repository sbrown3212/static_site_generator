import unittest

from generate_page import extract_title


class TestGeneratePage(unittest.TestCase):
    # Extract title function
    def test_extract_title(self):
        markdown = "# Hello"

        result = extract_title(markdown)
        expected = "Hello"
        self.assertEqual(expected, result)
    

    def test_extract_title_exception(self):
        markdown = "## This should raise an exception"

        with self.assertRaises(Exception):
            extract_title(markdown)
    

    def test_extract_title_exception2(self):
        markdown = "This too should raise an exception"

        with self.assertRaises(Exception):
            extract_title(markdown)
    

    # Generate page function


if __name__ == "__main__":
    unittest.main()