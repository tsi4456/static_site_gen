import unittest

from htmlnode import LeafNode, ParentNode


class TestParentNode(unittest.TestCase):
    def test_parent(self):
        node1 = LeafNode("p", "Hello, world!")
        node2 = LeafNode("div", "Section heading", {"class": "centered"})
        parent = ParentNode("span", [node1, node2], {"class": "container"})
        self.assertEqual(
            parent.to_html(),
            '<span class="container"><p>Hello, world!</p><div class="centered">Section heading</div></span>',
        )

    def test_parent_as_child(self):
        node1 = LeafNode("p", "Hello, world!")
        node2 = LeafNode("div", "Section heading", {"class": "centered"})
        parent = ParentNode("span", [node1, node2], {"class": "container"})
        grandparent = ParentNode("body", [node1, parent, node2])
        self.assertEqual(
            grandparent.to_html(),
            '<body><p>Hello, world!</p><span class="container"><p>Hello, world!</p><div class="centered">Section heading</div></span><div class="centered">Section heading</div></body>',
        )


if __name__ == "__main__":
    unittest.main()
