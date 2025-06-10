from textnode import TextType, TextNode
import re

DELIMS = {"**": TextType.BOLD, "_": TextType.ITALIC, "`": TextType.CODE}


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        node: TextNode
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        if len(sections := node.text.split(delimiter)) % 2:
            for i in range(len(sections)):
                if sections[i]:
                    if i % 2 == 0:
                        new_nodes.append(TextNode(sections[i], TextType.TEXT))
                    else:
                        new_nodes.append(TextNode(sections[i], text_type))
    return new_nodes


def extract_markdown_images(text: str):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)


def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)


def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        node: TextNode
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        text = node.text
        images = extract_markdown_images(node.text)
        if images:
            for image in images:
                new_text, text = text.split(f"![{image[0]}]({image[1]})")
                if new_text:
                    new_nodes.append(TextNode(new_text, TextType.TEXT))
                new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
        new_nodes.append(TextNode(text, TextType.TEXT))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        node: TextNode
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        text = node.text
        links = extract_markdown_links(node.text)
        if links:
            for link in links:
                new_text, text = text.split(f"[{link[0]}]({link[1]})")
                if new_text:
                    new_nodes.append(TextNode(new_text, TextType.TEXT))
                new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
        new_nodes.append(TextNode(text, TextType.TEXT))
    return new_nodes


def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    for delim, texttype in DELIMS.items():
        nodes = split_nodes_delimiter(nodes, delim, texttype)
    return nodes
