import sys
import os

def processFile(file_name):
    script_dir = os.path.abspath(os.getcwd())
    abs_file_path = os.path.join(script_dir, file_name)
    file = open(abs_file_path, "r").read()

def lox():
    args = sys.argv[1:]
    if(len(args) != 1):
        print("\033[91mFailed to run\nUsage: plox [script]")
        sys.exit(1)
    processFile(args[0])
    

if __name__ == '__main__':
    lox()