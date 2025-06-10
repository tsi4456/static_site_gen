import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_not_eq2(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node too!", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_url(self):
        node = TextNode("This is a text node", TextType.ITALIC, None)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertEqual(node, node2)

    def test_url2(self):
        node = TextNode("This is a text node", TextType.ITALIC, None)
        node2 = TextNode(
            "This is a text node", TextType.ITALIC, "http://www.google.com/"
        )
        self.assertNotEqual(node, node2)


class TestTextToHTMLNode(unittest.TestCase):
    def test_tth(self):
        node1 = TextNode("Bold text", TextType.BOLD)
        self.assertEqual(
            text_node_to_html_node(node1).to_html(),
            "<b>Bold text</b>",
        )


if __name__ == "__main__":
    unittest.main()
