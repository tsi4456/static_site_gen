from enum import Enum
from htmlnode import LeafNode
import re


class TextType(Enum):
    TEXT = "normal text"
    BOLD = "bold text"
    ITALIC = "italic text"
    CODE = "code text"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self, text: str, text_type: TextType, url: str = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return all(
            [
                self.text == other.text,
                self.text_type == other.text_type,
                self.url == other.url,
            ]
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(tag=None, value=re.sub(r"\s{2,}", " ", text_node.text))
        case TextType.BOLD:
            return LeafNode(tag="b", value=re.sub(r"\s{2,}", " ", text_node.text))
        case TextType.ITALIC:
            return LeafNode(tag="i", value=re.sub(r"\s{2,}", " ", text_node.text))
        case TextType.CODE:
            return LeafNode(tag="code", value=text_node.text.replace("\n", "\\n"))
        case TextType.LINK:
            return LeafNode(
                tag="a",
                value=re.sub(r"\s{2,}", " ", text_node.text),
                props={"href": text_node.url},
            )
        case TextType.IMAGE:
            return LeafNode(
                tag="img",
                props={
                    "src": text_node.url,
                    "alt": re.sub(r"\s{2,}", " ", text_node.text),
                },
            )
        case _:
            raise Exception("invalid node type")
