import unittest

from block_funcs import BlockType, markdown_to_blocks, block_to_block_type


class TestBlockToBlock(unittest.TestCase):
    def test_heading1(self):
        markdown = "# Heading 1"
        expected = BlockType.HEADING
        self.assertEqual(block_to_block_type(markdown), expected)

    def test_heading2(self):
        markdown = "## Heading 2"
        expected = BlockType.HEADING
        self.assertEqual(block_to_block_type(markdown), expected)

    def test_heading3(self):
        markdown = "### Heading 3"
        expected = BlockType.HEADING
        self.assertEqual(block_to_block_type(markdown), expected)

    def test_heading4(self):
        markdown = "#### Heading 4"
        expected = BlockType.HEADING
        self.assertEqual(block_to_block_type(markdown), expected)

    def test_heading5(self):
        markdown = "##### Heading 5"
        expected = BlockType.HEADING
        self.assertEqual(block_to_block_type(markdown), expected)

    def test_heading6(self):
        markdown = "###### Heading 6"
        expected = BlockType.HEADING
        self.assertEqual(block_to_block_type(markdown), expected)

    def test_code(self):
        markdown = """```
        This is a code block
        ```"""
        expected = BlockType.CODE
        self.assertEqual(block_to_block_type(markdown), expected)

    def test_quote(self):
        markdown = """> To be
> or not
> to be"""
        expected = BlockType.QUOTE
        self.assertEqual(block_to_block_type(markdown), expected)

    def test_ul(self):
        markdown = """- Item 1
- Item 2
- Item 3"""
        expected = BlockType.UL
        self.assertEqual(block_to_block_type(markdown), expected)

    def test_ol_pos(self):
        markdown = """1. This
2. Is
3. Ordered"""
        expected = BlockType.OL
        self.assertEqual(block_to_block_type(markdown), expected)

    def test_ol_neg(self):
        markdown = """1. This
3. Is
2. Ordered"""
        expected = BlockType.OL
        self.assertNotEqual(block_to_block_type(markdown), expected)

    def test_para(self):
        markdown = """1. This
3. Is
2. Ordered"""
        expected = BlockType.PARAGRAPH
        self.assertEqual(block_to_block_type(markdown), expected)

    def test_para(self):
        markdown = "Just a regular human block of text."
        expected = BlockType.PARAGRAPH
        self.assertEqual(block_to_block_type(markdown), expected)


if __name__ == "__main__":
    unittest.main()
