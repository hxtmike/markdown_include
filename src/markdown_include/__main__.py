import sys
from .markdown_include import markdown_include

def main():
    lenarg = len(sys.argv)
    if lenarg < 2 or lenarg > 3:
        print("Unexcepted Error: the argument should be '<input file> <output file>'")
        sys.exit()

    if lenarg == 2:
        markdown_include(sys.argv[1])

    if lenarg == 3:
        markdown_include(sys.argv[1], sys.argv[2])

if __name__ == '__main__':
    main()
