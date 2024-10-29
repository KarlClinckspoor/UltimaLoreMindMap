from pathlib import Path
from text_manipulation import add_yaml_header, replace_with_wikilinks

# fmt: off
filenames_and_tags = {
    "A LETTER TO NEW ACOLYTES.md":                          ["book", "u8", "official", "in-game"],
    "ADVENTURE QUARTERLY VOL. IX.md":                       ["book", "u8", "official", "in-game"],
    "ADVENTURE QUARTERLY VOL. XII.md":                      ["book", "u8", "official", "in-game"],
    "All books.md":                                         ["book", "u8", "official", "in-game"],
    "ALL SCROLLS.md":                                       ["book", "u8", "official", "in-game"],
    "BENTIC'S JOURNAL.md":                                  ["book", "u8", "official", "in-game"],
    "BROGDAN'S HELPFUL GUIDE TO MUSHROOMS.md":              ["book", "u8", "official", "in-game"],
    "CAPTAIN'S REPORT.md":                                  ["book", "u8", "official", "in-game"],
    "CATACOMB SCROLL.md":                                   ["book", "u8", "official", "in-game"],
    "DE-VENOMING THE KITH.md":                              ["book", "u8", "official", "in-game"],
    "DISPELLING MYTHS THE TRUTH ABOUT MAGIC.md":            ["book", "u8", "official", "in-game"],
    "EAR OF ARRICORN.md":                                   ["book", "u8", "official", "in-game"],
    "EARTHEN MAGIC.md":                                     ["book", "u8", "official", "in-game"],
    "ENEMIES OF TENEBRAE.md":                               ["book", "u8", "official", "in-game"],
    "EXPEDITION JOURNAL, BOOK II.md":                       ["book", "u8", "official", "in-game"],
    "EYE OF THE BOULDER, THE RUNES OF THE MYTH DRAINER.md": ["book", "u8", "official", "in-game"],
    "FINDING THE WISDOM OF STRATOS.md":                     ["book", "u8", "official", "in-game"],
    "GOLD VALUABLE COMMODITY OR WORTHLESS TRASH.md":        ["book", "u8", "official", "in-game"],
    "GUARD LOGS.md":                                        ["book", "u8", "official", "in-game"],
    "HISTORY OF PAGAN.md":                                  ["book", "u8", "official", "in-game"],
    "HONOR LOST.md":                                        ["book", "u8", "official", "in-game"],
    "JOURNAL OF VERAS THE HEALER.md":                       ["book", "u8", "official", "in-game"],
    "JOURNEYS THROUGH HELL.md":                             ["book", "u8", "official", "in-game"],
    "KILLER JOKES.md":                                      ["book", "u8", "official", "in-game"],
    "LETTER FROM MORDEA.md":                                ["book", "u8", "official", "in-game"],
    "LETTER TO MORDEA.md":                                  ["book", "u8", "official", "in-game"],
    "LOGBOOKS IN THE PIT OF EARTH.md":                      ["book", "u8", "official", "in-game"],
    "MAGIC ARMOUR.md":                                      ["book", "u8", "official", "in-game"],
    "MORIENS NECROMANCER, PROPHET, HERO.md":                ["book", "u8", "official", "in-game"],
    "MY RIVAL, MY LOVE - PART I.md":                        ["book", "u8", "official", "in-game"],
    "ON SORCEROUS WAYS.md":                                 ["book", "u8", "official", "in-game"],
    "PARABLES FROM THE TEACHINGS OF STRATOS, VOL. I.md":    ["book", "u8", "official", "in-game"],
    "PARABLES FROM THE TEACHINGS OF STRATOS, VOL. II.md":   ["book", "u8", "official", "in-game"],
    "POTIONS.md":                                           ["book", "u8", "official", "in-game"],
    "RAISING YOUR CHILDREN CORRECTLY.md":                   ["book", "u8", "official", "in-game"],
    "SAYINGS OF THE GUARDIAN.md":                           ["book", "u8", "official", "in-game"],
    "SCROLL.md":                                            ["book", "u8", "official", "in-game"],
    "SCROLLS FOUND ON THE QUEST FOR SLAYER.md":             ["book", "u8", "official", "in-game"],
    "SONG OF FRED.md":                                      ["book", "u8", "official", "in-game"],
    "SPELLBOOKS OF SORCERY.md":                             ["book", "u8", "official", "in-game"],
    "SPELLBOOKS OF THAUMATURGY.md":                         ["book", "u8", "official", "in-game"],
    "SPELLBOOKS OF THEURGY.md":                             ["book", "u8", "official", "in-game"],
    "STORIES TO MAKE CHILDREN SLEEP.md":                    ["book", "u8", "official", "in-game"],
    "THE ART OF FLAME.md":                                  ["book", "u8", "official", "in-game"],
    "THE BEAUTY OF RHIAN.md":                               ["book", "u8", "official", "in-game"],
    "THE BIG BOOK OF ADVENTURE.md":                         ["book", "u8", "official", "in-game"],
    "THE CHEESY BOOK.md":                                   ["book", "u8", "official", "in-game"],
    "THE CHRONICLE OF PAGAN.md":                            ["book", "u8", "official", "in-game"],
    "THE DESTRUCTION OF THE TEMPLE.md":                     ["book", "u8", "official", "in-game"],
    "THE FINAL SUNLIGHT.md":                                ["book", "u8", "official", "in-game"],
    "THE HISTORY OF NECROMANCY.md":                         ["book", "u8", "official", "in-game"],
    "THE MAGIC OF LOTHIAN.md":                              ["book", "u8", "official", "in-game"],
    "THE MYSTERIES OF LITHOS.md":                           ["book", "u8", "official", "in-game"],
    "THE MYTHOLOGY OF THE ZEALAN DEITIES.md":               ["book", "u8", "official", "in-game"],
    "THE OBJECTIVE HISTORY OF PAGAN.md":                    ["book", "u8", "official", "in-game"],
    "THE OFFICIAL LOGBOOK OF CRIMES AND PUNISHMENTS.md":    ["book", "u8", "official", "in-game"],
    "THE REAGENTS OF THAUMATURGY.md":                       ["book", "u8", "official", "in-game"],
    "THE SAGA OF BONE CRUSHER.md":                          ["book", "u8", "official", "in-game"],
    "THE TONGUE OF FLAME.md":                               ["book", "u8", "official", "in-game"],
    "THE VOICES OF MARY.md":                                ["book", "u8", "official", "in-game"],
    "THE WARRIOR AND THE ACOLYTE.md":                       ["book", "u8", "official", "in-game"],
    "TORAX SCROLL.md":                                      ["book", "u8", "official", "in-game"],
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
