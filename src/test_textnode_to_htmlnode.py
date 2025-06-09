import unittest

from htmlnode import text_node_to_html_node
from textnode import TextNode, TextType


class TestTextToHTMLNode(unittest.TestCase):
    def test_tth(self):
        node1 = TextNode("Bold text", TextType.BOLD)
        self.assertEqual(
            text_node_to_html_node(node1).to_html(),
            "<b>Bold text</b>",
        )


if __name__ == "__main__":
    unittest.main()
