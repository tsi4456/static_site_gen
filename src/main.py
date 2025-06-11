import shutil
import os
import block_funcs as bf

SOURCE_DIR = "static/"
PUBLIC_DIR = "public/"
CONTENT_DIR = "content/"


def main():
    dir_copy(SOURCE_DIR, PUBLIC_DIR)
    generate_pages_recursive(CONTENT_DIR, "template.html", PUBLIC_DIR)


def dir_copy(source, destination):
    if os.path.exists(destination):
        print("Removing existing data")
        shutil.rmtree(destination)
    if not os.path.exists(destination):
        print(f"Creating target directory: {destination}")
        os.mkdir(destination)
    contents = os.listdir(source)
    for file in contents:
        if os.path.isfile(filepath := os.path.join(source, file)):
            print(f"Copying {filepath}")
            shutil.copy(filepath, destination)
        elif os.path.isdir(filepath):
            dir_copy(filepath, os.path.join(destination, file))


def extract_title(markdown: str):
    for line in markdown.split("\n"):
        if line.startswith("# "):
            return line[2:].strip()
    raise Exception("header not found")


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r", encoding="utf-8") as f:
        markdown = f.read()

    with open(template_path, "r", encoding="utf-8") as f:
        template = f.read()

    content = bf.markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)

    page = template.replace("{{ Title }}", title).replace("{{ Content }}", content)

    if not os.path.exists(dir := os.path.dirname(dest_path)):
        os.makedirs(dir)
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(page)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    if not os.path.exists(dir_path_content):
        raise Exception("invalid file path")

    for file in os.listdir(dir_path_content):
        if os.path.isfile((filepath := os.path.join(dir_path_content, file))):
            filename, extension = file.split(".")
            if extension == "md":
                generate_page(
                    filepath,
                    template_path,
                    os.path.join(dest_dir_path, filename + ".html"),
                )
        elif os.path.isdir(filepath):
            generate_pages_recursive(
                filepath,
                template_path,
                os.path.join(dest_dir_path, file),
            )


if __name__ == "__main__":
    main()
