import os
import regex as re
from collections import Counter
from pathlib import Path
from nltk.corpus import words, wordnet
from nltk.stem import WordNetLemmatizer as wnl


def tokenize(text):
    text = re.sub(r"[^\w\s]", "", text)
    return text.split()


def find_words_in_folder(
    folder_path: Path,
    rare_words_file: Path,
    proper_names_file: Path,
    all_words_file_sorted_by_count: Path,
    rare_threshold=5,
):
    word_counter = Counter()
    proper_names = set()

    # Pattern to match capitalized words not at the start of sentences
    proper_name_pattern = re.compile(r"(?<![.!?]\s|^)\b[A-Z][a-z]+\b")

    for filename in folder_path.glob("*.md"):
        content = filename.read_text(encoding="utf-8")
        proper_names.update(proper_name_pattern.findall(content))
        words = tokenize(content.lower())
        word_counter.update(words)

    rare_words = [word for word, count in word_counter.items() if count <= rare_threshold]

    rare_words_file.write_text("\n".join(rare_words), encoding="utf-8")
    proper_names_file.write_text("\n".join(sorted(list(proper_names))), encoding="utf-8")

    # Sorting the entire collection by frequency
    word_num = [(word, num) for word, num in word_counter.items()]
    word_num.sort(key=lambda x: x[1], reverse=True)
    all_words_file_sorted_by_count.write_text(
        "\n".join([f"{word}" for word, _ in word_num]), encoding="utf-8"
    )


def tag_english_words(file_path: Path, output_file: Path):
    english_vocab = set(words.words())
    lines = file_path.read_text(encoding="utf-8").split("\n")

    with open(output_file, "w", encoding="utf-8") as output:
        for line in lines:
            word = line.strip()  # Remove any extra whitespace/newlines
            # Add an asterisk if the word is in the English vocabulary
            # if word.lower() in english_vocab:
            if wnl().lemmatize(word.lower()) in english_vocab:
                output.write(f"* {word}\n")
            else:
                output.write(f"{word}\n")
