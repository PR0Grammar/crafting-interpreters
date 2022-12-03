import sys
import os

def printError(msg):
    print('\033[91m'+msg)

def error(line: "int", msg: "str"):
    template = "[line: {0}] Error: {1}"
    printError(template.format(line, msg))
    sys.exit(1)

def run(lines: "list[str]") -> "None":
    return None

def processFile(file_name):
    script_dir = os.path.abspath(os.getcwd())
    abs_file_path = os.path.join(script_dir, file_name)
    lines = open(abs_file_path, "r").readlines()
    run(lines)

def lox():
    args = sys.argv[1:]
    if len(args) != 1:
        printError("Failed to run\nUsage: plox [script]")
        sys.exit(1)
    processFile(args[0])

if __name__ == "__main__":
    lox()
