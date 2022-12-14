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

- The last step is to convert the instructions into a form the machine can actually run. In other words, __generating code__ or __code gen__. This form is (usually) not human-readable friendly.

- The question here: do we generate instructions for a real CPU or a virtual one?
    - Generating instructions for a chip's language also means the compiler is tied to a specific architecture
    - With __virtual machines__, the generated code for them are known as __bytecode__ (because each instruction is often a byte long). The synthetic insturctions are designed to map a little more closely to the language's semantics, and not tied so much to any architecture.

### Virtual Machines

- With bytecode, the job isn't done. We still need instructions that the CPU can understand. We could write a mini-compiler for each target architecture. This way, the bytecode acts as an Intermediate Representation

- OR, we can write a __virtual machine__ (VM), a program that _emulates_ a hypothetical chip supporting the virtual architecture at runtime.
    - This is slower than compiling to native code as every instruction needs to be simulated at runtime to execute.
    - In exchange, you get simplicity and portability. The language just needs a corresponding VM, not having to worry about the underlying architecture.

### Runtime

- If we compile into machine code, we simply tell the OS to load the executable and do its thing.

- If we compile into byecode, we need to start up the VM and load the program into it.

- In many languages, except maybe very low-level languages, we may need _services_ to operate. For example, auto memory management will require a garbage collector. 

- The __runtime__ is basically all these "services" that get added. In a fully compiled language, it gets inserted in the executable (eg. Go). For bytecode, the VM or interpreter contains the code (eg. Java, Python, JS).


## Shortcuts and Alternate Routes

### Single-pass Compilers

- Some simple compilers interleave parsing, analysis and code gen so that they produce output code directly in the parser, without syntax trees or IRs in the middle.

- __Single-pass compilers__ restrict the design of the language - no intermediate data structures to store global info about the program and you don't revisit any previously parsed code. (eg. C, Pascal)

- In the old days, memory was precious. Compilers might not even be able to hold an _entire source file_, let alone the entire program.

### Tree-walk Interpreters

- Some PLs execute code right after parsing it to an AST. To run the program, the interpreter traverses the syntax tree one branch and leaf at a time, evaluating teach ndoe as it goes along.

- Not widely used for general purpose PLs since it tends to be slow. 

### Transpilers

- __Transpilers__, formly called __source to source compilers__ or __transcompilers__, translates languages to another language that is "just as high of a level."

- If tooling already exist for language A to compile into a lower language, then language B may not have to do the tedious as well - if we can go from B -> A, we can go from B -> lower level language

- Back in the day, as UNIX gained fame, lots of compilers produced C as their output code since C was everywhere UNIX was. Today's "modern machine" is the web brwoser, and its language is JavaScript (for better or for worse). Many languages these days target JS since its the main way to get your code running in the browser (and now mobile phones, desktop apps, VR, toaster ovens?)

- The more dissimilar two languages are, the more phases of a typical full compiler you will see (eg. analysis, optimization)

### Just in time compilation

- The fastest way to execute code is by compiling it to machine code, but you might not know what architecture your end user's machine supports. What do you do?

- You can compile it to native for the architecture that the computer supports when the program is loaded. (eg. from JS source directly, or bytecode for JVM, CLR). This is called __just in time compilation__, or __JIT compilation__.

- Some advanced JITs embed mechanisms to to see what areas are hotspots, and recompile them with more advanced optimizations.

## Compilers and Interpreters

- __Compiling__ is an implementation technique that translates some source language to another - typically lower level. (this includes transpiling, bytecode generation, machine code generation, etc)

- __Interpreters__ is an implementation technique that takes source code and executes it immediately. It runs the program "from source."

- Compilers don't execute the code that they output after transforming.

- Its not always easy to distinguish when something is a compiler or an interpreter. Sometimes, they are both!

- Compilers: javac, gcc, Typescript, CoffeeScript, Rust, clang

- Interpreters: MRI(Ruby), PHP3

- Hazy Middle: C#, Go, Scala, Lua, CPython, V8 (JS), Haskell, PHP4, YARV(Ruby)



