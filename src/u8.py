from pathlib import Path
from text_manipulation import add_yaml_header, replace_with_wikilinks

# fmt: off
filenames_and_tags = {
    "A LETTER TO NEW ACOLYTES.md":                          ["book", "u8"],
    "ADVENTURE QUARTERLY VOL. IX.md":                       ["book", "u8"],
    "ADVENTURE QUARTERLY VOL. XII.md":                      ["book", "u8"],
    "All books.md":                                         ["book", "u8"],
    "ALL SCROLLS.md":                                       ["book", "u8"],
    "BENTIC'S JOURNAL.md":                                  ["book", "u8"],
    "BROGDAN'S HELPFUL GUIDE TO MUSHROOMS.md":              ["book", "u8"],
    "CAPTAIN'S REPORT.md":                                  ["book", "u8"],
    "CATACOMB SCROLL.md":                                   ["book", "u8"],
    "DE-VENOMING THE KITH.md":                              ["book", "u8"],
    "DISPELLING MYTHS THE TRUTH ABOUT MAGIC.md":            ["book", "u8"],
    "EAR OF ARRICORN.md":                                   ["book", "u8"],
    "EARTHEN MAGIC.md":                                     ["book", "u8"],
    "ENEMIES OF TENEBRAE.md":                               ["book", "u8"],
    "EXPEDITION JOURNAL, BOOK II.md":                       ["book", "u8"],
    "EYE OF THE BOULDER, THE RUNES OF THE MYTH DRAINER.md": ["book", "u8"],
    "FINDING THE WISDOM OF STRATOS.md":                     ["book", "u8"],
    "GOLD VALUABLE COMMODITY OR WORTHLESS TRASH.md":        ["book", "u8"],
    "GUARD LOGS.md":                                        ["book", "u8"],
    "HISTORY OF PAGAN.md":                                  ["book", "u8"],
    "HONOR LOST.md":                                        ["book", "u8"],
    "JOURNAL OF VERAS THE HEALER.md":                       ["book", "u8"],
    "JOURNEYS THROUGH HELL.md":                             ["book", "u8"],
    "KILLER JOKES.md":                                      ["book", "u8"],
    "LETTER FROM MORDEA.md":                                ["book", "u8"],
    "LETTER TO MORDEA.md":                                  ["book", "u8"],
    "LOGBOOKS IN THE PIT OF EARTH.md":                      ["book", "u8"],
    "MAGIC ARMOUR.md":                                      ["book", "u8"],
    "MORIENS NECROMANCER, PROPHET, HERO.md":                ["book", "u8"],
    "MY RIVAL, MY LOVE - PART I.md":                        ["book", "u8"],
    "ON SORCEROUS WAYS.md":                                 ["book", "u8"],
    "PARABLES FROM THE TEACHINGS OF STRATOS, VOL. I.md":    ["book", "u8"],
    "PARABLES FROM THE TEACHINGS OF STRATOS, VOL. II.md":   ["book", "u8"],
    "POTIONS.md":                                           ["book", "u8"],
    "RAISING YOUR CHILDREN CORRECTLY.md":                   ["book", "u8"],
    "SAYINGS OF THE GUARDIAN.md":                           ["book", "u8"],
    "SCROLL.md":                                            ["book", "u8"],
    "SCROLLS FOUND ON THE QUEST FOR SLAYER.md":             ["book", "u8"],
    "SONG OF FRED.md":                                      ["book", "u8"],
    "SPELLBOOKS OF SORCERY.md":                             ["book", "u8"],
    "SPELLBOOKS OF THAUMATURGY.md":                         ["book", "u8"],
    "SPELLBOOKS OF THEURGY.md":                             ["book", "u8"],
    "STORIES TO MAKE CHILDREN SLEEP.md":                    ["book", "u8"],
    "THE ART OF FLAME.md":                                  ["book", "u8"],
    "THE BEAUTY OF RHIAN.md":                               ["book", "u8"],
    "THE BIG BOOK OF ADVENTURE.md":                         ["book", "u8"],
    "THE CHEESY BOOK.md":                                   ["book", "u8"],
    "THE CHRONICLE OF PAGAN.md":                            ["book", "u8"],
    "THE DESTRUCTION OF THE TEMPLE.md":                     ["book", "u8"],
    "THE FINAL SUNLIGHT.md":                                ["book", "u8"],
    "THE HISTORY OF NECROMANCY.md":                         ["book", "u8"],
    "THE MAGIC OF LOTHIAN.md":                              ["book", "u8"],
    "THE MYSTERIES OF LITHOS.md":                           ["book", "u8"],
    "THE MYTHOLOGY OF THE ZEALAN DEITIES.md":               ["book", "u8"],
    "THE OBJECTIVE HISTORY OF PAGAN.md":                    ["book", "u8"],
    "THE OFFICIAL LOGBOOK OF CRIMES AND PUNISHMENTS.md":    ["book", "u8"],
    "THE REAGENTS OF THAUMATURGY.md":                       ["book", "u8"],
    "THE SAGA OF BONE CRUSHER.md":                          ["book", "u8"],
    "THE TONGUE OF FLAME.md":                               ["book", "u8"],
    "THE VOICES OF MARY.md":                                ["book", "u8"],
    "THE WARRIOR AND THE ACOLYTE.md":                       ["book", "u8"],
    "TORAX SCROLL.md":                                      ["book", "u8"],
}
# fmt: on

md_destination = Path("../Wikilinked/u8")
md_destination.mkdir(exist_ok=True, parents=True)
md_source = Path("../Original/u8")
wordlist = set(
    Path("../wordlists/u8/manual_additions.txt").read_text().split("\n")
    + Path("../wordlists/u8/proper_names.txt").read_text().split("\n")
    # + Path("../wordlists/u8/rare_words.txt").read_text().split("\n")
)

for md in md_source.glob("*.md"):
    destination_path = md_destination / md.name
    content = "\n".join(md.read_text(encoding="utf-8").split("\n")[1:])
    content = add_yaml_header(
        replace_with_wikilinks(content, wordlist),
        filenames_and_tags[md.name],
        md.stem,
    )
    destination_path.write_text(content, encoding="utf-8")
