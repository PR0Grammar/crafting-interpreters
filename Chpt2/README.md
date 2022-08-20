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

- Where can we store away the analysis?:
    - Attributes on the syntax treee itself (extra fields in the nodes that aren't initialized during parsing but filled in later)
    - Table lookup (__symbol table__)
    - Transform tree into a new data structure that directly expresses the semantics of the code

### Intermediate Representations

- You can think of compilers as a pipeliene where each stage's job is to organize the data representing the user's code in such as way that makes the NEXT stage simpler to implement

- Somewhere in the middle, the code may get stored in an "intermediate form" - __Intermediate Representation__ (IR) - that isn't tightly coupled to either the src or dest forms. Rather, it acts as an interface between two languages

    - Rather than having to create a FULL compiler for each langauge you want to compile down to some instruction set (eg. Pascal -> x86, C -> ARM), you can have each language use a SHARED IR, which lets all "front end" of the source language focus on getting into the IR form and the "back end" focus on targeting each architecture.

### Optimizations

- Once we understand what a user's program means, we can __optimize__ the end result. We can swap different logic that has the __same semnatics__ but implements it more efficiently

```python
    x = 1 + 2 + 3 * 0
```

Compiler can evaluate and reduce this to:
```python
    x = 3
```

- Optimization is a huge part of PLs - many hackers spent their entire time just squeezing additional drops of performance. It makes a huge difference if the language is widely adopted.

### Code Generation

