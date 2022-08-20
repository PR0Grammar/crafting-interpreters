# A Map of the Territory

## Parts of a Language

### Scanning

- Scanning, aka Lexing, or Lexical Analysis

- A __scanner__ takes a linear stream of chars and chunks them together into a series of __tokens__

- Tokens can be single characters, like (, or several characters like numbers, string literals, and identifiers

- Some chars in source file don't actually mean anything. Whitespace and comments are often insignificant for example


### Parsing

- This is where our syntax gets a __grammar__ - the ability to compose larger expression and statements of smaller parts.

- A __parser__ takes the flat sequence of tokens and builds a tree - a __parse tree__, or __abstract syntax tree__ (AST)

