# Scanning

- The first step of any compiler or interpreter is __scanning__.

- The scanner takes raw source code as a series of characters and groups into into a series of chunks called __tokens__ (meaningful "words" or "punctuations")

- Scanners are pretty much a `switch` statement - they just need to handle every valid case

## The Interpreter Framework

### Error handling

- Many textbooks gloss over error handling since its more of a practical matter rather than CS problem

- When the user's code is working, they aren't thinking about the langauge at all - their headspace is all about _the program_. When things are wrong, they start to notice the implementation. 

## Lexemes and Tokens

- Our job in lexical analysis is to scan through the list of characters and group them together in small sequences that still represent something.

- Each of these "blobs" of characters is called a lexemes. **The lexemes are only the raw substrings of the source code. Tokens are the "type" of that lexeme**. 

    - eg) lexeme="var" <> token="VARIABLE"
          lexeme="<=" <> token="LESS_THAN_EQUAL_TO_COMP"
    
    - There are many classifications for token types: 
        - single-character: left_paran, right_paran, dot, minus, plus, etc
        - one or two characters: equal, equal_equal, greater_than, etc
        - literals: identifier, string, number
        - keywords: and, class, else, false, fun, return, super, true, etc.

### Location Info

- As noted previously, its important to tell users _where_ the errors occured. Tracking it within the `Token` class
will help.

- Some interpreters that are more sophisticated can include column, length and line, but to keep it simple, we will only include the line


## Regular Languages and Expressions

- The rules that determine how a particular language groups characters into lexemes are called its **lexical grammar**.

- Most programming languages have rules of lexical grammar that are simple enough to be classified as a **regular language**.


## Recognizing Lexemes

### Maximal munch

- When two lexical grammar rules can both match a piece of code that the scanner is loking at, whichever one matches the most characters wins.

```Python

# for keyword
for

# forgo variable - most characters, so we should assume variable, not "for"
forgo
```