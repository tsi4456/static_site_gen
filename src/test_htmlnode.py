import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props(self):
        node = HTMLNode(
            props={
                "href": "https://www.google.com",
                "target": "_blank",
            }
        )
        result = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), result)

    def test_empty_props(self):
        node = HTMLNode()
        result = ""
        self.assertEqual(node.props_to_html(), result)

    def test_repr_tag_text(self):
        node = HTMLNode(tag="div", value="Page body text.")
        result = "HTMLNode(div, Page body text., None, None)"
        self.assertEqual(str(node), result)

    def test_empty(self):
        node = HTMLNode()
        result = "HTMLNode(None, None, None, None)"
        self.assertEqual(str(node), result)


if __name__ == "__main__":
    unittest.main()
