from pathlib import Path
from text_manipulation import add_yaml_header, replace_with_wikilinks

# fmt: off
filenames_and_tags = {
    Path(r"books\A LETTER TO NEW ACOLYTES.md"):                          ["book", "u8", "official", "in-game"],
    Path("books\ADVENTURE QUARTERLY VOL. IX.md"):                        ["book", "u8", "official", "in-game"],
    Path("books\ADVENTURE QUARTERLY VOL. XII.md"):                       ["book", "u8", "official", "in-game"],
    Path(r"books\BENTIC'S JOURNAL.md"):                                  ["book", "u8", "official", "in-game"],
    Path(r"books\BROGDAN'S HELPFUL GUIDE TO MUSHROOMS.md"):              ["book", "u8", "official", "in-game"],
    Path(r"books\CAPTAIN'S REPORT.md"):                                   ["book", "u8", "official", "in-game"],
    Path(r"books\CATACOMB SCROLL.md"):                                   ["book", "u8", "official", "in-game"],
    Path(r"books\DE-VENOMING THE KITH.md"):                              ["book", "u8", "official", "in-game"],
    Path(r"books\DISPELLING MYTHS THE TRUTH ABOUT MAGIC.md"):            ["book", "u8", "official", "in-game"],
    Path(r"books\EAR OF ARRICORN.md"):                                   ["book", "u8", "official", "in-game"],
    Path(r"books\EARTHEN MAGIC.md"):                                     ["book", "u8", "official", "in-game"],
    Path(r"books\ENEMIES OF TENEBRAE.md"):                               ["book", "u8", "official", "in-game"],
    Path(r"books\EXPEDITION JOURNAL, BOOK II.md"):                       ["book", "u8", "official", "in-game"],
    Path(r"books\EYE OF THE BOULDER, THE RUNES OF THE MYTH DRAINER.md"): ["book", "u8", "official", "in-game"],
    Path(r"books\FINDING THE WISDOM OF STRATOS.md"):                     ["book", "u8", "official", "in-game"],
    Path(r"books\GOLD VALUABLE COMMODITY OR WORTHLESS TRASH.md"):        ["book", "u8", "official", "in-game"],
    Path(r"books\GUARD LOGS.md"):                                        ["book", "u8", "official", "in-game"],
    Path(r"books\HISTORY OF PAGAN.md"):                                  ["book", "u8", "official", "in-game"],
    Path(r"books\HONOR LOST.md"):                                        ["book", "u8", "official", "in-game"],
    Path(r"books\JOURNAL OF VERAS THE HEALER.md"):                       ["book", "u8", "official", "in-game"],
    Path(r"books\JOURNEYS THROUGH HELL.md"):                             ["book", "u8", "official", "in-game"],
    Path(r"books\KILLER JOKES.md"):                                      ["book", "u8", "official", "in-game"],
    Path(r"books\LETTER FROM MORDEA.md"):                                ["book", "u8", "official", "in-game"],
    Path(r"books\LETTER TO MORDEA.md"):                                  ["book", "u8", "official", "in-game"],
    Path(r"books\LOGBOOKS IN THE PIT OF EARTH.md"):                      ["book", "u8", "official", "in-game"],
    Path(r"books\MAGIC ARMOUR.md"):                                      ["book", "u8", "official", "in-game"],
    Path(r"books\MORIENS NECROMANCER, PROPHET, HERO.md"):                ["book", "u8", "official", "in-game"],
    Path(r"books\MY RIVAL, MY LOVE - PART I.md"):                        ["book", "u8", "official", "in-game"],
    Path(r"books\ON SORCEROUS WAYS.md"):                                 ["book", "u8", "official", "in-game"],
    Path(r"books\PARABLES FROM THE TEACHINGS OF STRATOS, VOL. I.md"):    ["book", "u8", "official", "in-game"],
    Path(r"books\PARABLES FROM THE TEACHINGS OF STRATOS, VOL. II.md"):   ["book", "u8", "official", "in-game"],
    Path(r"books\POTIONS.md"):                                           ["book", "u8", "official", "in-game"],
    Path(r"books\RAISING YOUR CHILDREN CORRECTLY.md"):                   ["book", "u8", "official", "in-game"],
    Path(r"books\SAYINGS OF THE GUARDIAN.md"):                           ["book", "u8", "official", "in-game"],
    Path(r"books\SCROLL.md"):                                            ["book", "u8", "official", "in-game"],
    Path(r"books\SCROLLS FOUND ON THE QUEST FOR SLAYER.md"):             ["book", "u8", "official", "in-game"],
    Path(r"books\SONG OF FRED.md"):                                      ["book", "u8", "official", "in-game"],
    Path(r"books\SPELLBOOKS OF SORCERY.md"):                             ["book", "u8", "official", "in-game"],
    Path(r"books\SPELLBOOKS OF THAUMATURGY.md"):                         ["book", "u8", "official", "in-game"],
    Path(r"books\SPELLBOOKS OF THEURGY.md"):                             ["book", "u8", "official", "in-game"],
    Path(r"books\STORIES TO MAKE CHILDREN SLEEP.md"):                    ["book", "u8", "official", "in-game"],
    Path(r"books\THE ART OF FLAME.md"):                                  ["book", "u8", "official", "in-game"],
    Path(r"books\THE BEAUTY OF RHIAN.md"):                               ["book", "u8", "official", "in-game"],
    Path(r"books\THE BIG BOOK OF ADVENTURE.md"):                         ["book", "u8", "official", "in-game"],
    Path(r"books\THE CHEESY BOOK.md"):                                   ["book", "u8", "official", "in-game"],
    Path(r"books\THE CHRONICLE OF PAGAN.md"):                            ["book", "u8", "official", "in-game"],
    Path(r"books\THE DESTRUCTION OF THE TEMPLE.md"):                     ["book", "u8", "official", "in-game"],
    Path(r"books\THE FINAL SUNLIGHT.md"):                                ["book", "u8", "official", "in-game"],
    Path(r"books\THE HISTORY OF NECROMANCY.md"):                         ["book", "u8", "official", "in-game"],
    Path(r"books\THE MAGIC OF LOTHIAN.md"):                              ["book", "u8", "official", "in-game"],
    Path(r"books\THE MYSTERIES OF LITHOS.md"):                           ["book", "u8", "official", "in-game"],
    Path(r"books\THE MYTHOLOGY OF THE ZEALAN DEITIES.md"):               ["book", "u8", "official", "in-game"],
    Path(r"books\THE OBJECTIVE HISTORY OF PAGAN.md"):                    ["book", "u8", "official", "in-game"],
    Path(r"books\THE OFFICIAL LOGBOOK OF CRIMES AND PUNISHMENTS.md"):    ["book", "u8", "official", "in-game"],
    Path(r"books\THE REAGENTS OF THAUMATURGY.md"):                       ["book", "u8", "official", "in-game"],
    Path(r"books\THE SAGA OF BONE CRUSHER.md"):                          ["book", "u8", "official", "in-game"],
    Path(r"books\THE TONGUE OF FLAME.md"):                               ["book", "u8", "official", "in-game"],
    Path(r"books\THE VOICES OF MARY.md"):                                ["book", "u8", "official", "in-game"],
    Path(r"books\THE WARRIOR AND THE ACOLYTE.md"):                       ["book", "u8", "official", "in-game"],
    Path(r"books\TORAX SCROLL.md"):                                      ["book", "u8", "official", "in-game"],
    Path("chronicles.txt"):                                              ["u8", "official", "manual", "out-game"],
    Path("cluebook.txt"):                                                ["u8", "official", "out-game"],
    Path("lostvale.txt"):                                                ["u8", "lostvale", "design-docs", "out-game"],
    Path("prima.txt"):                                                   ["u8", "unofficial", "design-docs", "out-game"],
    Path(r"dialogue\ARAMINA.txt"):                                       ["dialogue", "u8", "official", "in-game"],
    Path(r"dialogue\ARCADION.txt"):                                      ["dialogue", "u8", "official", "in-game"],
    Path(r"dialogue\AVATAR.txt"):                                        ["dialogue", "u8", "official", "in-game"],
    Path(r"dialogue\BANE.txt"):                                          ["dialogue", "u8", "official", "in-game"],
    Path(r"dialogue\BENTIC.txt"):                                        ["dialogue", "u8", "official", "in-game"],
    Path(r"dialogue\BEREN.txt"):                                         ["dialogue", "u8", "official", "in-game"],
    Path(r"dialogue\CARDAS.txt"):                                        ["dialogue", "u8", "official", "in-game"],
    Path(r"dialogue\CORINTH.txt"):                                       ["dialogue", "u8", "official", "in-game"],
    Path(r"dialogue\CYRRUS.txt"):                                        ["dialogue", "u8", "official", "in-game"],
    Path(r"dialogue\DAEMOS.txt"):                                        ["dialogue", "u8", "official", "in-game"],
    Path(r"dialogue\DARION.txt"):                                        ["dialogue", "u8", "official", "in-game"],
    Path(r"dialogue\DEVON.txt"):                                         ["dialogue", "u8", "official", "in-game"],
    Path(r"dialogue\EMRICHOL.txt"):                                      ["dialogue", "u8", "official", "in-game"],
    Path(r"dialogue\ENDHYDRO.txt"):                                      ["dialogue", "u8", "official", "in-game"],
    Path(r"dialogue\ENDLITH.txt"):                                       ["dialogue", "u8", "official", "in-game"],
    Path(r"dialogue\ENDPYRO.txt"):                                       ["dialogue", "u8", "official", "in-game"],
    Path(r"dialogue\EVILSORC.txt"):                                      ["dialogue", "u8", "official", "in-game"],
    Path(r"dialogue\GORGROND.txt"):                                      ["dialogue", "u8", "official", "in-game"],
    Path(r"dialogue\GUARD1.txt"):                                        ["dialogue", "u8", "official", "in-game"],
    Path(r"dialogue\GUARD10.txt"):                                       ["dialogue", "u8", "official", "in-game"],
    Path(r"dialogue\GUARD2.txt"):                                        ["dialogue", "u8", "official", "in-game"],
    Path(r"dialogue\GUARD3.txt"):                                        ["dialogue", "u8", "official", "in-game"],
    Path(r"dialogue\GUARD4.txt"):                                        ["dialogue", "u8", "official", "in-game"],
    Path(r"dialogue\GUARD5.txt"):                                        ["dialogue", "u8", "official", "in-game"],
    Path(r"dialogue\GUARD6.txt"):                                        ["dialogue", "u8", "official", "in-game"],
    Path(r"dialogue\GUARD7.txt"):                                        ["dialogue", "u8", "official", "in-game"],
    Path(r"dialogue\GUARD8.txt"):                                        ["dialogue", "u8", "official", "in-game"],
    Path(r"dialogue\GUARD9.txt"):                                        ["dialogue", "u8", "official", "in-game"],
    Path(r"dialogue\GWILLIM.txt"):                                       ["dialogue", "u8", "official", "in-game"],
    Path(r"dialogue\JENNA.txt"):                                         ["dialogue", "u8", "official", "in-game"],
    Path(r"dialogue\KILANDRA.txt"):                                      ["dialogue", "u8", "official", "in-game"],
    Path(r"dialogue\KORICK.txt"):                                        ["dialogue", "u8", "official", "in-game"],
    Path(r"dialogue\KOTHIUS.txt"):                                       ["dialogue", "u8", "official", "in-game"],
    Path(r"dialogue\MALCHIR.txt"):                                       ["dialogue", "u8", "official", "in-game"],
    Path(r"dialogue\MENTAR.txt"):                                        ["dialogue", "u8", "official", "in-game"],
    Path(r"dialogue\MORDEA.txt"):                                        ["dialogue", "u8", "official", "in-game"],
    Path(r"dialogue\MYTHRAN.txt"):                                       ["dialogue", "u8", "official", "in-game"],
    Path(r"dialogue\ORLOK.txt"):                                         ["dialogue", "u8", "official", "in-game"],
    Path(r"dialogue\RHIAN.txt"):                                         ["dialogue", "u8", "official", "in-game"],
    Path(r"dialogue\SALKIND.txt"):                                       ["dialogue", "u8", "official", "in-game"],
    Path(r"dialogue\SHAANA.txt"):                                        ["dialogue", "u8", "official", "in-game"],
    Path(r"dialogue\STELLOS.txt"):                                       ["dialogue", "u8", "official", "in-game"],
    Path(r"dialogue\TALLON.txt"):                                        ["dialogue", "u8", "official", "in-game"],
    Path(r"dialogue\TARNA.txt"):                                         ["dialogue", "u8", "official", "in-game"],
    Path(r"dialogue\TORWIN.txt"):                                        ["dialogue", "u8", "official", "in-game"],
    Path(r"dialogue\VARDION.txt"):                                       ["dialogue", "u8", "official", "in-game"],
    Path(r"dialogue\VIVIDOS.txt"):                                       ["dialogue", "u8", "official", "in-game"],
    Path(r"dialogue\XAVIER.txt"):                                        ["dialogue", "u8", "official", "in-game"],
}
# fmt: on

md_destination = Path("../Wikilinked/u8")
md_destination.mkdir(exist_ok=True, parents=True)
md_source = Path("../Original/u8")
wordlist = list(
    set(
        Path("../wordlists/u8/manual_additions.txt")
        .read_text()
        .split("\n")
        # + Path("../wordlists/u8/proper_names.txt").read_text().split("\n")
        # + Path("../wordlists/u8/rare_words.txt").read_text().split("\n")
    )
)
wordlist.sort(key=len, reverse=True)

for filepath, tags in filenames_and_tags.items():
    destination_path = md_destination / filepath.name
    content = "\n".join((md_source / filepath).read_text(encoding="utf-8").split("\n"))
    content = add_yaml_header(
        replace_with_wikilinks(content, wordlist),
        tags,
        filepath.stem,
    )
    destination_path.write_text(content, encoding="utf-8")
