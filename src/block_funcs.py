from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import text_node_to_html_node, TextNode, TextType
from inline_funcs import text_to_textnodes
from enum import Enum
import re


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UL = "unordered list"
    OL = "ordered list"


def markdown_to_blocks(markdown: str) -> list:
    return filter(lambda b: b, [block.strip() for block in markdown.split("\n\n")])


def block_to_block_type(markdown: str) -> BlockType:
    if re.match(r"^#{1,6} \S", markdown):
        return BlockType.HEADING
    if markdown.startswith("```") and markdown.endswith("```"):
        return BlockType.CODE
    lines = markdown.split("\n")
    if all(list(map(lambda x: x.startswith(">"), lines))):
        return BlockType.QUOTE
    if all(list(map(lambda x: x.startswith("- "), lines))):
        return BlockType.UL
    is_ol = False
    for i in range(len(lines)):
        if (num := re.match(r"^(\d+). ", lines[i])) and int(num[1]) == i + 1:
            is_ol = True
        else:
            is_ol = False
            break
    return BlockType.OL if is_ol else BlockType.PARAGRAPH


def text_to_children(markdown) -> list:
    return [text_node_to_html_node(node) for node in text_to_textnodes(markdown)]


def markdown_to_html_node(markdown) -> ParentNode:
    new_nodes = []
    for block in markdown_to_blocks(markdown):
        block: str
        match block_to_block_type(block):
            case BlockType.HEADING:
                head, text = block.split(" ", maxsplit=1)
                new_nodes.append(ParentNode(f"h{len(head)}", text_to_children(text)))

            case BlockType.CODE:
                new_nodes.append(
                    ParentNode(
                        "pre",
                        [text_node_to_html_node(TextNode(block[4:-3], TextType.CODE))],
                    )
                )

            case BlockType.QUOTE:
                new_nodes.append(
                    ParentNode(
                        "blockquote",
                        text_to_children(
                            " ".join(
                                [line.lstrip(">").strip() for line in block.split("\n")]
                            )
                        ),
                    )
                )

            case BlockType.UL:
                new_nodes.append(
                    ParentNode(
                        "ul",
                        [
                            ParentNode(
                                "li",
                                text_to_children(line[2:].strip()),
                            )
                            for line in block.split("\n")
                        ],
                    )
                )

            case BlockType.OL:
                new_nodes.append(
                    ParentNode(
                        "ol",
                        [
                            ParentNode(
                                "li", text_to_children(line.split(" ", maxsplit=1)[1])
                            )
                            for line in block.split("\n")
                        ],
                    )
                )
            case BlockType.PARAGRAPH:
                new_nodes.append(ParentNode("p", text_to_children(block)))
            case _:
                raise Exception("invalid block type")
    return ParentNode("div", new_nodes)
