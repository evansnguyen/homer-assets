from pathlib import Path

def generate_img_tag(file):
    return f'<img src="assets/{file.name}" alt="{file.stem}" width="50">'

def get_files(extensions):
    all_files = []
    for ext in extensions:
        all_files.extend(Path('./assets').glob(ext))
    return sorted(all_files)

if __name__ == "__main__":
    imgs = get_files(('*.png', '*.jpg', '*.svg'))
    img_tags = [generate_img_tag(x) for x in imgs]

    with open("README.md", "wt", encoding="UTF-8") as f:
        f.write("# Homer Icons\n\n")
        f.write("[Homer Icons](https://github.com/evansnguyen/homer-icons)\n\n")
        f.write(" ".join(img_tags))
        f.write("\n")
