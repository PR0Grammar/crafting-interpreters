import sys
import os
from token_type import TokenType
import scanner

def printError(msg):
    print('\033[91m'+msg)

def error(line: "int", msg: "str"):
    template = "[line: {0}] Error: {1}"
    printError(template.format(line, msg))
    sys.exit(1)

def run(raw_file_content: str) -> "None":
    lox_scanner = scanner.Scanner(raw_file_content)

    tokens = lox_scanner.scan_tokens()
    for t in tokens:
        print(TokenType(t.token_type).name)
    return None

def processFile(file_name):
    script_dir = os.path.abspath(os.getcwd())
    abs_file_path = os.path.join(script_dir, file_name)
    file = open(abs_file_path, "r").read()
    run(file)

def lox():
    args = sys.argv[1:]
    if len(args) != 1:
        printError("Failed to run\nUsage: python3 lox [relative_path]")
        sys.exit(1)
    processFile(args[0])


# eg. python3 lox/lox.py lox/test_files/valid_mixed.lox
if __name__ == "__main__":
    lox()
