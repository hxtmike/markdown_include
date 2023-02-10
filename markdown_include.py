#!/usr/bin/env python3

import re
import sys

def markdown_include(inputFile: str, outputFile: str=None) -> None: 
    # define default output filename
    if outputFile == None:
        indexPeriod = inputFile.rfind('.')

        if indexPeriod == -1:
            prefix = inputFile
            suffix = ''
        else:
            prefix = inputFile[:indexPeriod]
            suffix = inputFile[indexPeriod:]

        outputFile = prefix + '_mdincl_output' + suffix
        # print(outputFile)
    
    # fine the relative dir of the inputFile
    indexSlash = inputFile.rfind("/")
    if indexSlash == -1:
        directory = "./"
    else:
        directory = inputFile[:indexSlash+1]
    # print(directory)

    try:
        with open(inputFile, 'r') as file:
            content = file.read()
    except:
        print('Unexcepted Error: input file read error')
        sys.exit()

    # print(content)
    # print("#" * 50)
    includes = re.findall(r'<!-- include \((.*)\) -->', content)

    for include in includes:
        try:
            # print(directory+include)
            with open(directory + include, 'r') as file:
                includeContent = file.read()
                # print(includeContent)
                # print("#" * 50)
        except:
            print('Unexcepted Error: included file cannot be found')
            sys.exit()
        
        content = content.replace('<!-- include ({}) -->'.format(include), includeContent)
    
    with open(outputFile, 'w') as file:
        file.write(content)

if __name__ == '__main__':
    lenarg = len(sys.argv)
    if lenarg < 2 or lenarg > 3 :
        print("Unexcepted Error: the argument should be '<input file> <output file>'")
        sys.exit()
    
    if lenarg == 2:
        markdown_include(sys.argv[1])
    
    if lenarg == 3:
        markdown_include(sys.argv[1], sys.argv[2])
