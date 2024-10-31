import regex as re
from pathlib import Path


# Function to replace words with wiki-style links
def replace_with_wikilinks(content: str, words: set[str] | list[str]) -> str:
    for word in words:
        content = re.sub(rf"(\b{re.escape(word)}\b)(?![^\[\]]*\])", f"[[{word}]]", content)
    return content


def add_yaml_header(content: str, tags: list[str], title: str) -> str:
    formatted_tags = "tags:\n"
    formatted_tags += "\n".join([f"- {tag}" for tag in tags])
    new_content = f"---\ntitle: {title}\n{formatted_tags}\n---\n\n{content}"
    return new_content
