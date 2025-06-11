# from textnode import TextNode, TextType
from block_funcs import markdown_to_html_node

# from htmlnode import HTMLNode, LeafNode, ParentNode
import block_funcs


def main():
    md = """
    This is **bolded** paragraph
    text in a p
    tag here

    This is another paragraph with _italic_ text and `code` here

    """

    md2 = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

    print(markdown_to_html_node(md).to_html())


if __name__ == "__main__":
    main()
