# Scanning

- The first step of any compiler or interpreter is __scanning__.

- The scanner takes raw source code as a series of characters and groups into into a series of chunks called __tokens__ (meaningful "words" or "punctuations")

- Scanners are pretty much a `switch` statement.

## The Interpreter Framework

### Error handling

- Many textbooks gloss over error handling since its more of a practical matter rather than CS problem

- When the user's code is working, they aren't thinking about the langauge at all - their headspace is all about _the program_. When things are wrong, they start to notice the implementation. 

### Lexemes and Tokens

- Our job in lexical analysis is to scan through the list of characters and group them together in small sequences that still represent something.

- Each of these "blobs" of characters is called a lexemes. **The lexemes are only the raw substrings of the source code. Tokens are the "type" of that lexeme**. 

    - eg) lexeme="var" <> token="VARIABLE"
          lexeme=="<=" <> token="LESS_THAN_EQUAL_TO_COMP"