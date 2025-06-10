from textnode import TextNode, TextType

# from htmlnode import HTMLNode, LeafNode, ParentNode
import node_funcs


def main():
    # tn = TextNode("lorem ipsum", TextType.ITALIC, None)
    # print(tn)

    # ln = LeafNode("p", "Paragraph")
    # ln2 = LeafNode(None, "Raw text")

    # pn = ParentNode("div", [ln, ln2])

    # print(pn.to_html())

    # node = TextNode("This is text with a `code block` word", TextType.TEXT)
    # new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

    # node = TextNode(
    #     "This is text with a link [to boot dev](https://www.boot.dev) and an image ![to youtube](https://www.youtube.com/@bootdotdev), isn't that great?",
    #     TextType.TEXT,
    # )
    # new_nodes = node_funcs.split_nodes_image([node])
    # new_nodes1 = node_funcs.split_nodes_link([node])

    # [
    #     TextNode("This is text with a link ", TextType.TEXT),
    #     TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
    #     TextNode(" and ", TextType.TEXT),
    #     TextNode(
    #         "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
    #     ),
    # ]

    # for node in new_nodes:
    #     print(node)

    text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"

    for node in node_funcs.text_to_textnodes(text):
        print(node)


if __name__ == "__main__":
    main()
