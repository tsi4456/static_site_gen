from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode


def main():
    tn = TextNode("lorem ipsum", TextType.ITALIC, None)
    print(tn)

    ln = LeafNode("p", "Paragraph")
    ln2 = LeafNode(None, "Raw text")

    pn = ParentNode("div", [ln, ln2])

    print(pn.to_html())


if __name__ == "__main__":
    main()
