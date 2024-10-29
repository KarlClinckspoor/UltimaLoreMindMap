# Ultima Lore mind map

## Intro

This is a repo that gets the written contents of Ultima games, processes them, and adds wikilinks to the files
so they can be loaded into a program like [Obsidian](https://obsidian.md).

## Contributing

Areas to contribute:

* Getting the text content of the games into .md files, and supplying them with tags, not in the files, but
  in the python files specific to each game, in the `src` folder.

| Game           | Books               | Dialogue | Other | Status      |
|----------------|---------------------|----------|-------|-------------|
| Akalabeth      | TODO                | TODO     | TODO  | In progress |
| Ultima 1       | TODO                | TODO     | TODO  | In progress |  
| Ultima 2       | TODO                | TODO     | TODO  | In progress |  
| Ultima 3       | TODO                | TODO     | TODO  | In progress |  
| Ultima 4       | TODO                | TODO     | TODO  | In progress |  
| Ultima 5       | TODO                | TODO     | TODO  | In progress |  
| Ultima 6       | TODO                | TODO     | TODO  | In progress |  
| Ultima 7       | TODO                | TODO     | TODO  | In progress |  
| Ultima 7-2     | TODO                | TODO     | TODO  | In progress |  
| Ultima 8       | Wordlist refinement | TODO     | TODO  | In progress |  
| Ultima 9       | TODO                | TODO     | TODO  | In progress |  
| Underworld 1   | TODO                | TODO     | TODO  | In progress |  
| Underworld 2   | TODO                | TODO     | TODO  | In progress |  
| Martian Dreams | TODO                | TODO     | TODO  | In progress |  
| Savage Empire  | TODO                | TODO     | TODO  | In progress |  


* Running the tools to extract some word lists of the files, parsing through the word lists, removing and
  adding a few as needed.
* Revising and improving the Python tools.
  * Formatter is `black`, line length is 100 characters.
  * Avoid inserting dependencies when possible.
  * `nltk` with the `popular` corpus is used. `pip` install it, then `python -c "import nltk; nltk.download('popular')"`

## Possible inclusions

* Official manuals
* Official cluebooks

## Acknowledgements

[Notable Ultima](https://www.notableultima.com/) as the source of many of these files.