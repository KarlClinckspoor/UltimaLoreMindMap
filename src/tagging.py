from pathlib import Path
from wordlist_creation import tag_english_words, find_words_in_folder, tokenize

THRESHOLD = 5
originals = Path("../Original/U8")
wordlists = Path("../wordlists/temp/u8")
wordlists.mkdir(parents=True, exist_ok=True)

find_words_in_folder(
    originals,
    wordlists / "rare_words.txt",
    wordlists / "proper_names.txt",
    wordlists / "all_words.txt",
    rare_threshold=THRESHOLD,
)
tag_english_words(
    wordlists / "rare_words.txt",
    wordlists / "tagged_rare_words.txt",
)
tag_english_words(
    wordlists / "proper_names.txt",
    wordlists / "tagged_proper_names.txt",
)
tag_english_words(
    wordlists / "all_words.txt",
    wordlists / "tagged_all_words.txt",
)
