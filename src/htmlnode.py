from textnode import TextNode, TextType


class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props:
            return "".join([f' {key}="{value}"' for key, value in self.props.items()])
        return ""


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        if not value:
            raise ValueError("leaf nodes must have a value")
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self) -> str:
        return f'{"<"+self.tag+self.props_to_html()+">" if self.tag else ""}{self.value}{"</"+self.tag+">" if self.tag else ""}'


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        if not tag:
            raise ValueError("parent nodes must have a tag")
        if not children:
            raise ValueError("parent nodes must have children")
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        return f'{"<"+self.tag+self.props_to_html()+">" if self.tag else ""}{"".join([c.to_html() for c in self.children])}{"</"+self.tag+">" if self.tag else ""}'


def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(value=text_node.text)
        case TextType.BOLD:
            return LeafNode(tag="b", value=text_node.text)
        case TextType.ITALIC:
            return LeafNode(tag="i", value=text_node.text)
        case TextType.CODE:
            return LeafNode(tag="code", value=text_node.text)
        case TextType.LINK:
            return LeafNode(
                tag="a", value=text_node.text, props={"href": text_node.url}
            )
        case TextType.IMAGE:
            return LeafNode(
                tag="img", props={"src": text_node.url, "alt": text_node.text}
            )
        case _:
            raise Exception("invalid node type")
