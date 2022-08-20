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

- Parsers also tell us when we use the grammers incorrectly by reporting __syntax errors__

### Static Analysis

- The first bit of analysis most languages do is called __binding__ or __resolution__. For each __indentifier__, we find out where the name is defined. This is where __scope__ comes into play - the region of source code where a certain name can be used to refer to a certain declartion

- If the language is statically typed, we can report __type errors__. If for instance you are adding _a_ and _b_, once they are declared, we can see if addition between their types is allowed.

